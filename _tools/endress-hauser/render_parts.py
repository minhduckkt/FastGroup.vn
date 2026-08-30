# -*- coding: utf-8 -*-
"""Cac khoi HTML dung lai: the san pham, bang thong so, FAQ tu sinh."""
import sys, os, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gen_lib as g

SPEC_LABELS = [
    ('sku',                'Mã model'),
    ('name',               'Tên đầy đủ'),
    ('family',             'Dòng sản phẩm'),
    ('category',           'Nhóm kỹ thuật'),
    ('measuring_principle','Nguyên lý đo'),
    ('measuring_range',    'Dải đo'),
    ('accuracy',           'Độ chính xác'),
    ('process_temp',       'Nhiệt độ quá trình'),
    ('process_pressure',   'Áp suất quá trình'),
    ('process_connection', 'Kết nối quá trình'),
    ('wetted_parts',       'Vật liệu tiếp xúc'),
    ('output_comm',        'Tín hiệu / truyền thông'),
    ('key_features',       'Tính năng nổi bật'),
    ('approvals',          'Chứng nhận / phê duyệt'),
    ('source_pdf',         'Nguồn dữ liệu'),
]

# vai gia tri boilerplate trong catalog doc rat la khi dat giua trang tieng Viet
_DISPLAY = {
    'None (non-invasive)': 'Không có — thiết bị không tiếp xúc môi chất (non-invasive)',
    'Non-contact (sensor mounted outside vessel)': 'Không tiếp xúc — cảm biến lắp ngoài thành bồn',
}

def clean(v):
    v = (v or '').strip()
    if v in ('', '-', 'N/A', 'n/a'):
        return ''
    return _DISPLAY.get(v, v)

def spec_table(p):
    rows = []
    for k, label in SPEC_LABELS:
        v = clean(p.get(k))
        if v:
            rows.append('<div class="spec-row"><span>%s</span><strong>%s</strong></div>' % (g.e(label), g.e(v)))
    return '<div class="spec-table">%s</div>' % ''.join(rows)

def quick_facts(p):
    pairs = [('Mã model', p['sku']), ('Nhóm đo', p['catalog_vi'])]
    for k, lb in (('measuring_principle','Nguyên lý'), ('measuring_range','Dải đo'),
                  ('output_comm','Tín hiệu ra'), ('process_temp','Nhiệt độ quá trình')):
        v = clean(p.get(k))
        if v and len(pairs) < 6:
            pairs.append((lb, v))
    return '<div class="quick-facts">%s</div>' % ''.join(
        '<div><span>%s</span><strong>%s</strong></div>' % (g.e(a), g.e(b)) for a, b in pairs)

def product_card(p, up, cls_extra=''):
    sub = clean(p.get('short_desc')) or clean(p.get('measuring_principle')) or p['catalog_vi']
    return ('<article class="product-card %(tone)s %(x)s"><a class="product-media" href="%(up)s%(url)s">'
            '<img src="%(up)sassets/products/%(img)s" alt="%(t)s — %(cat)s Endress+Hauser chính hãng" loading="lazy" /></a>'
            '<div class="product-body"><div class="product-meta">%(cat)s</div>'
            '<h3><a href="%(up)s%(url)s">%(t)s</a></h3><p>%(sub)s</p>'
            '<p class="meta-line">Mã: %(sku)s</p></div></article>') % dict(
        tone=p['tone'], x=cls_extra, up=up, url=p['url'], img=p['img'], t=g.e(p['title']),
        cat=g.e(p['category']), sub=g.e(sub), sku=g.e(p['sku']))

def product_grid(items, up):
    return '<div class="product-grid">%s</div>' % ''.join(product_card(p, up) for p in items)

def product_table(items, up):
    head = ('<div class="table-wrap"><table class="product-table"><thead><tr>'
            '<th>Model</th><th>Nguyên lý</th><th>Dải đo</th><th>Nhiệt độ quá trình</th><th>Tín hiệu ra</th>'
            '</tr></thead><tbody>')
    body = []
    for p in items:
        body.append(
            '<tr><td><div class="table-product"><span class="product-thumb">'
            '<img src="%(up)sassets/products/%(img)s" alt="%(t)s" loading="lazy" /></span>'
            '<span><a href="%(up)s%(url)s">%(t)s</a><small>%(cat)s</small></span></div></td>'
            '<td>%(pr)s</td><td>%(rg)s</td><td>%(tp)s</td><td>%(ou)s</td></tr>' % dict(
                up=up, img=p['img'], t=g.e(p['title']), url=p['url'], cat=g.e(p['category']),
                pr=g.e(clean(p.get('measuring_principle')) or '—'),
                rg=g.e(clean(p.get('measuring_range')) or '—'),
                tp=g.e(clean(p.get('process_temp')) or '—'),
                ou=g.e(clean(p.get('output_comm')) or '—')))
    return head + ''.join(body) + '</tbody></table></div>'

def product_faq(p):
    t, sku = p['title'], p['sku']
    faq = [
        ('%s dùng cho ứng dụng nào?' % t,
         '%s thuộc nhóm %s (%s). Fast Group Engineering hỗ trợ đối chiếu điều kiện quá trình thực tế — môi chất, '
         'nhiệt độ, áp suất, kết nối sẵn có — để xác nhận model phù hợp trước khi báo giá.'
         % (t, p['category'], p['catalog_vi'])),
        ('Mua %s chính hãng ở đâu tại Việt Nam?' % sku,
         'Anh/chị gửi RFQ cho Fast Group Engineering để kiểm tra nguồn hàng Endress+Hauser chính hãng, xác nhận cấu hình '
         'theo mã đặt hàng, lead time và chứng từ CO/CQ giao tại Việt Nam.'),
        ('Thông số trên trang này có phải thông số cuối cùng không?',
         'Không. Dữ liệu được trích từ catalog chính thức của Endress+Hauser và dùng để tra cứu nhanh. Dải đo, độ chính xác, '
         'giới hạn nhiệt độ và áp suất phụ thuộc phiên bản và cấu hình đặt hàng — cần đối chiếu Technical Information (TI) '
         'đúng mã đặt hàng trên endress.com trước khi chốt.'),
        ('Website có công bố giá %s không?' % sku,
         'Không. Giá thiết bị đo lường phụ thuộc cấu hình, số lượng, chứng nhận và lead time từng lô, nên Fast Group báo giá '
         'theo RFQ thay vì công bố giá không có nguồn hoặc đã hết hiệu lực.'),
    ]
    return faq

def product_ld(p):
    desc = (clean(p.get('short_desc')) + '. ' if clean(p.get('short_desc')) else '') + \
           ('Nguyên lý %s. ' % clean(p.get('measuring_principle')) if clean(p.get('measuring_principle')) else '') + \
           'Endress+Hauser chính hãng, Fast Group Engineering cung cấp tại Việt Nam.'
    props = []
    for k, lb in (('measuring_principle','Nguyên lý đo'), ('measuring_range','Dải đo'),
                  ('process_temp','Nhiệt độ quá trình'), ('process_pressure','Áp suất quá trình'),
                  ('process_connection','Kết nối quá trình'), ('wetted_parts','Vật liệu tiếp xúc'),
                  ('output_comm','Tín hiệu / truyền thông'), ('approvals','Chứng nhận')):
        v = clean(p.get(k))
        if v:
            props.append({"@type":"PropertyValue","name":lb,"value":v})
    ld = {"@context":"https://schema.org","@type":"Product","name":p['title'],
          "sku":p['sku'],"mpn":p['sku'],
          "brand":{"@type":"Brand","name":"Endress+Hauser"},
          "category":p['category'],
          "image":g.BASE+'assets/products/'+p['img'],
          "description":desc, "url":p['abs'],
          "seller":{"@type":"Organization","name":g.OWNER,"url":g.ROOT},
          "offers":{"@type":"Offer","url":p['abs'],"availability":"https://schema.org/InStock",
                    "priceCurrency":"VND",
                    "seller":{"@type":"Organization","name":g.OWNER},
                    "priceSpecification":{"@type":"PriceSpecification","priceCurrency":"VND",
                        "description":"Báo giá theo RFQ, cấu hình, số lượng và chứng từ yêu cầu."}}}
    if clean(p.get('name')) and clean(p['name']) != p['title']:
        ld["alternateName"] = clean(p['name'])
    if props:
        ld["additionalProperty"] = props
    return ld
