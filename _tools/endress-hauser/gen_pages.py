# -*- coding: utf-8 -*-
"""Sinh tung loai trang cua mini-site Endress+Hauser Viet Nam."""
import sys, os, re, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gen_lib as g
import render_parts as R
import diagrams as D
from data_layer import OUT

def page(head_html, up, hubs, body):
    return head_html + g.header(up, hubs) + '<main>' + body + '</main>' + g.footer(up, hubs)

# ---------------------------------------------------------------- product
def build_product(p, hubs, byslug, all_products):
    up = '../../'
    parent = byslug[p['tech']] if p['tech'] else byslug[p['main']]
    main = byslug[p['main']]
    desc = ('%s — %s. %s Endress+Hauser chính hãng, Fast Group Engineering cung cấp tại Việt Nam, '
            'tư vấn cấu hình và báo giá theo RFQ kèm CO/CQ.') % (
            p['title'], R.clean(p.get('short_desc')) or p['category'], p['catalog_vi'])
    desc = re.sub(r'\s+', ' ', desc)[:300]
    title = '%s | %s Endress+Hauser chính hãng — Fast Group' % (p['title'], p['catalog_vi'])
    faq = R.product_faq(p)
    trail = [('%s' % g.SITE, g.BASE), (parent['name'], g.BASE + parent['slug'] + '/'), (p['title'], p['abs'])]
    lds = [R.product_ld(p), g.bc_ld(trail), g.faq_ld(faq)]
    hd = g.head(title, desc, p['abs'], up, image=g.BASE + 'assets/products/' + p['img'],
                extra_ld=lds, og_type='product')

    # san pham lien quan
    pool = [x for x in parent['items'] if x['sku'] != p['sku']]
    same_cat = [x for x in pool if x['category'] == p['category']]
    rel = (same_cat + [x for x in pool if x not in same_cat])[:4]

    posts = p.get('posts') or []
    art_block = ''
    if posts:
        art_block = ('<div class="article-insight"><h2>Tài liệu kỹ thuật về %s</h2><p>%s</p>'
                     '<p><a href="%sblog/%s/">Đọc bài đầy đủ: %s</a></p></div>') % (
            g.e(p['title']), g.e(posts[0]['meta'].get('meta_description','')),
            up, posts[0]['slug'], g.e(posts[0]['meta'].get('title','')))

    body = []
    body.append(g.breadcrumb_bar(up, [('', 'Trang chủ'), (parent['slug'] + '/', parent['name']), (None, p['title'])]))
    body.append(
        '<section class="product-hero"><div class="container product-hero-grid"><div class="product-hero-copy">'
        '<div class="eyebrow">Endress+Hauser chính hãng · %s</div>'
        '<h1>%s — %s</h1><p class="lead">%s</p>'
        '<div class="hero-actions"><a class="button button-primary" href="#yeu-cau-bao-gia">Yêu cầu báo giá</a>'
        '<a class="button button-secondary" href="#thong-so">Xem thông số</a></div>%s</div>'
        '<figure class="product-visual"><img src="%sassets/products/%s" alt="%s — %s Endress+Hauser chính hãng" '
        'fetchpriority="high" /><figcaption>Ảnh sản phẩm %s — nguồn catalog Endress+Hauser</figcaption></figure>'
        '</div></section>' % (
            g.e(parent['name']), g.e(p['title']), g.e(R.clean(p.get('short_desc')) or p['category']),
            g.e(desc), R.quick_facts(p), up, p['img'], g.e(p['title']), g.e(p['category']), g.e(p['title'])))

    intro = ('<p><strong>%s</strong> thuộc nhóm %s trong danh mục %s của Endress+Hauser. %s</p>'
             '<p>Fast Group Engineering cung cấp %s chính hãng tại Việt Nam cho nhà máy, nhà thầu EPC và đơn vị tích hợp '
             'hệ thống: đối chiếu datasheet theo đúng mã đặt hàng, tư vấn chọn dải đo — kết nối quá trình — vật liệu tiếp xúc '
             'theo điều kiện vận hành thực tế, kiểm tra yêu cầu chứng nhận và hỗ trợ nhập khẩu kèm CO/CQ.</p>') % (
            g.e(p['title']), g.e(p['category']), g.e(p['catalog_vi']),
            g.e((R.clean(p.get('key_features')) + '.') if R.clean(p.get('key_features')) else ''), g.e(p['sku']))

    body.append(
        '<section class="section"><div class="container split"><div>'
        '<div class="section-heading"><div class="kicker">Giới thiệu</div><h2>%s trong ứng dụng %s</h2></div>%s%s'
        '<div class="article-insight caution"><h2>Cần đối chiếu datasheet trước khi đặt hàng</h2>'
        '<p>Thông số hiển thị ở đây trích từ catalog tổng của Endress+Hauser và dùng để tra cứu nhanh. Dải đo, độ chính xác, '
        'giới hạn nhiệt độ và áp suất thay đổi theo phiên bản và cấu hình đặt hàng — trước khi chốt mã, cần đối chiếu '
        'Technical Information (TI) đúng mã đặt hàng trên endress.com.</p></div></div>'
        '<aside class="quote-panel" id="yeu-cau-bao-gia"><div class="kicker">RFQ Endress+Hauser</div>'
        '<h2>Yêu cầu báo giá %s</h2><p>Gửi mã model kèm điều kiện quá trình để Fast Group xác nhận cấu hình, giá và lead time.</p>'
        '<ul class="quote-list"><li>Mã model: <strong>%s</strong></li><li>Nhóm đo: %s</li>'
        '<li>Môi chất, nhiệt độ và áp suất làm việc</li><li>Kết nối quá trình sẵn có trên thiết bị</li>'
        '<li>Yêu cầu chứng nhận phòng nổ, CO/CQ</li></ul>'
        '<a class="button button-primary" href="%slien-he/?model=%s">Gửi RFQ ngay</a></aside></div></section>' % (
            g.e(p['title']), g.e(p['catalog_vi']), intro, art_block,
            g.e(p['title']), g.e(p['sku']), g.e(p['catalog_vi']), up,
            g.e(p['sku'].replace(' ', '%20'))))

    body.append('<section class="section section-soft" id="thong-so"><div class="container">'
                '<div class="section-heading"><div class="kicker">Thông tin kỹ thuật</div>'
                '<h2>Thông số %s theo catalog Endress+Hauser</h2>'
                '<p>Chỉ hiển thị các trường có trong dữ liệu catalog gốc; trường trống nghĩa là catalog tổng không nêu, '
                'cần tra Technical Information của model.</p></div>%s</div></section>' % (
                g.e(p['sku']), R.spec_table(p)))

    body.append('<section class="section"><div class="container">'
                '<div class="section-heading"><div class="kicker">Chọn cấu hình</div>'
                '<h2>Bốn thông tin quyết định cấu hình %s</h2></div>'
                '<ul class="check-list">'
                '<li><strong>Điều kiện quá trình:</strong> môi chất, nhiệt độ và áp suất làm việc — quyết định phiên bản và vật liệu.</li>'
                '<li><strong>Kết nối quá trình:</strong> ren hay mặt bích, tiêu chuẩn và kích thước sẵn có trên thiết bị.</li>'
                '<li><strong>Tín hiệu và giao thức:</strong> phải khớp với hệ điều khiển hiện hữu (4–20 mA, HART, PROFIBUS PA, '
                'FOUNDATION Fieldbus, PROFINET/APL).</li>'
                '<li><strong>Chứng nhận:</strong> phòng nổ ATEX/IECEx, an toàn chức năng, chứng nhận vệ sinh nếu là ngành thực phẩm — dược.</li>'
                '</ul><p style="margin-top:22px"><a class="button button-secondary" href="%s%s/">Xem toàn bộ nhóm %s</a></p>'
                '</div></section>' % (g.e(p['title']), up, parent['slug'], g.e(parent['name'])))

    body.append('<section class="section section-soft"><div class="container">'
                '<div class="section-heading"><div class="kicker">Câu hỏi thường gặp</div>'
                '<h2>Mua %s chính hãng tại Việt Nam</h2></div>%s</div></section>' % (g.e(p['sku']), g.faq_html(faq)))

    if rel:
        body.append('<section class="section"><div class="container">'
                    '<div class="section-heading"><div class="kicker">Sản phẩm liên quan</div>'
                    '<h2>Model Endress+Hauser cùng nhóm</h2></div>%s</div></section>' % R.product_grid(rel, up))

    g.write(os.path.join(OUT, 'san-pham', p['slug'], 'index.html'),
            page(hd, up, hubs, ''.join(body)))

# ---------------------------------------------------------------- hub
def hub_faq(h):
    return [
        ('%s gồm những dòng sản phẩm nào?' % h['name'],
         'Trang này liệt kê %d model Endress+Hauser thuộc nhóm %s, kèm nguyên lý đo, dải đo, nhiệt độ quá trình và tín hiệu ra '
         'để so sánh nhanh trước khi vào datasheet chi tiết.' % (len(h['items']), h['name'])),
        ('Làm sao chọn đúng model trong nhóm này?',
         'Bắt đầu từ điều kiện quá trình: môi chất, nhiệt độ, áp suất và kết nối sẵn có trên thiết bị. Bốn thông tin này thường '
         'loại trừ được phần lớn model và chỉ còn một hoặc hai lựa chọn để so sánh chi tiết.'),
        ('Fast Group có báo giá theo model hay theo cấu hình?',
         'Theo cấu hình. Cùng một model nhưng khác kết nối quá trình, vật liệu tiếp xúc và chứng nhận thì giá và lead time '
         'khác nhau đáng kể, nên báo giá luôn gắn với mã đặt hàng cụ thể.'),
    ]

def build_hub(h, hubs, byslug, posts):
    up = '../'
    m = h['meta']
    canon = g.BASE + h['slug'] + '/'
    title = '%s | Fast Group' % m.get('meta_title', h['name'])
    desc = m.get('meta_desc', '')
    faq = hub_faq(h)
    trail = [(g.SITE, g.BASE)]
    if h['kind'] == 'tech':
        par = byslug[h['parent']]
        trail.append((par['name'], g.BASE + par['slug'] + '/'))
    trail.append((h['name'], canon))
    item_ld = {"@context":"https://schema.org","@type":"ItemList","name":h['name'],
               "numberOfItems":len(h['items']),
               "itemListElement":[{"@type":"ListItem","position":i+1,"url":x['abs'],"name":x['title']}
                                  for i, x in enumerate(h['items'])]}
    _hs = h.get('hero_sku')
    _hit = [x for x in h['items'] if x['sku'] == _hs]
    hero_img = _hit[0]['img'] if _hit else (h['items'][0]['img'] if h['items'] else 'eh-fmr51.png')
    hd = g.head(title, desc, canon, up,
                image=g.BASE + 'assets/products/' + hero_img,
                extra_ld=[g.bc_ld(trail), item_ld, g.faq_ld(faq)])

    bcrumb = [('', 'Trang chủ')]
    if h['kind'] == 'tech':
        bcrumb.append((byslug[h['parent']]['slug'] + '/', byslug[h['parent']]['name']))
    bcrumb.append((None, h['name']))

    body = [g.breadcrumb_bar(up, bcrumb)]
    body.append('<section class="hero hero-slim" style="--hero-image:url(\'/endress-hauser-viet-nam/assets/hero/%s\')">'
                '<div class="container hero-inner"><div class="hero-copy">'
                '<div class="eyebrow">%s</div><h1>%s</h1><p class="lead">%s</p>'
                '<div class="hero-actions"><a class="button button-primary" href="%slien-he/">Gửi RFQ</a>'
                '<a class="button button-secondary" href="#danh-sach">Xem %d model</a></div>'
                '</div></div></section>' % (
                hero_img, g.e(m.get('eyebrow','')), g.e(m.get('h1', h['name'])),
                g.e(m.get('lead','')), up, len(h['items'])))

    # cac hub con (chi voi hub chinh)
    subs = [x for x in hubs if x['kind'] == 'tech' and x.get('parent') == h['slug']]
    sub_html = ''
    if subs:
        sub_html = ('<div class="article-insight"><h2>Đi sâu theo công nghệ đo</h2><div class="hub-grid">%s</div></div>'
                    % ''.join('<a href="%s%s/">%s <span style="font-weight:600;color:var(--muted)">· %d model</span></a>'
                              % (up, s['slug'], g.e(s['name']), len(s['items'])) for s in subs))

    hub_diagram = D.diagram_for_hub(h)
    body.append('<section class="section"><div class="container"><article class="article-body hub-article">%s%s%s</article></div></section>'
                % (sub_html, hub_diagram, g.md(h['body'])))

    # danh sach san pham
    by_cat = {}
    for p in h['items']:
        by_cat.setdefault(p['category'], []).append(p)
    blocks = []
    for cat, items in sorted(by_cat.items()):
        blocks.append('<div class="section-heading" style="margin:34px 0 18px"><h2 style="font-size:1.5rem">%s '
                      '<span style="color:var(--muted);font-weight:600">· %d model</span></h2></div>%s'
                      % (g.e(cat), len(items), R.product_table(items, up)))
    body.append('<section class="section section-soft" id="danh-sach"><div class="container">'
                '<div class="section-heading"><div class="kicker">Danh sách model</div>'
                '<h2>%d model %s trong catalog Endress+Hauser</h2>'
                '<p>Bấm vào tên model để xem trang chi tiết với đầy đủ thông số theo catalog và biểu mẫu gửi RFQ.</p>'
                '</div>%s</div></section>' % (len(h['items']), g.e(h['name']), ''.join(blocks)))

    # bai viet lien quan
    rel_posts = [ps for ps in posts if ps['product'] is not None and
                 (ps['product']['tech'] == h['slug'] or ps['product']['main'] == h['slug'])][:4]
    if rel_posts:
        cards = ''.join('<article class="card"><div class="product-meta">%s</div><h3><a href="%sblog/%s/">%s</a></h3>'
                        '<p>%s</p></article>' % (g.e(ps['kw']), up, ps['slug'],
                                                 g.e(ps['meta'].get('title','')),
                                                 g.e(ps['meta'].get('meta_description','')))
                        for ps in rel_posts)
        body.append('<section class="section"><div class="container">'
                    '<div class="section-heading"><div class="kicker">Kiến thức đo lường</div>'
                    '<h2>Tài liệu kỹ thuật liên quan</h2></div><div class="grid grid-4">%s</div>'
                    '<p class="center" style="margin-top:26px"><a class="button button-secondary" href="%sblog/">'
                    'Xem tất cả bài kiến thức đo lường</a></p></div></section>' % (cards, up))

    body.append('<section class="section section-soft"><div class="container">'
                '<div class="section-heading"><div class="kicker">Câu hỏi thường gặp</div>'
                '<h2>%s — hỏi đáp nhanh</h2></div>%s</div></section>' % (g.e(h['name']), g.faq_html(faq)))

    g.write(os.path.join(OUT, h['slug'], 'index.html'), page(hd, up, hubs, ''.join(body)))

# ---------------------------------------------------------------- blog
def build_post(ps, hubs, byslug, all_posts):
    up = '../../'
    m = ps['meta']
    slug = ps['slug']
    canon = g.BASE + 'blog/%s/' % slug
    p = ps['product']
    parent = byslug[p['tech']] if p and p['tech'] else (byslug[p['main']] if p else None)
    img = p['img'] if p else 'eh-fmr51.png'
    title = m.get('meta_title') or m.get('title')
    desc = m.get('meta_description', '')
    kws = m.get('secondary_keywords') or []
    if isinstance(kws, str):
        kws = [kws]

    art_ld = {"@context":"https://schema.org","@type":"Article",
              "headline": m.get('title',''), "description": desc,
              "image": g.BASE + 'assets/products/' + img,
              "inLanguage":"vi", "mainEntityOfPage": canon,
              "author":{"@type":"Organization","name":g.OWNER,"url":g.ROOT},
              "publisher":{"@type":"Organization","name":g.OWNER,
                           "logo":{"@type":"ImageObject","url":g.ROOT+"img/logo.png"}},
              "datePublished": g.BUILD, "dateModified": g.BUILD,
              "keywords": ', '.join([m.get('primary_keyword','')] + list(kws))}
    trail = [(g.SITE, g.BASE), ('Kiến thức đo lường', g.BASE + 'blog/'), (m.get('title',''), canon)]
    hd = g.head('%s | Fast Group' % title, desc, canon, up,
                image=g.BASE + 'assets/products/' + img,
                extra_ld=[art_ld, g.bc_ld(trail)], og_type='article')

    body = []
    body.append('<section class="page-hero category-hero" style="--page-image:url(\'/endress-hauser-viet-nam/assets/hero/%s\')">'
                '<div class="container page-hero-inner">'
                '<nav class="breadcrumb"><a href="%s">%s</a><span>/</span><a href="%sblog/">Kiến thức đo lường</a>'
                '<span>/</span><span>%s</span></nav>'
                '<div class="eyebrow">%s · %s</div><h1>%s</h1><p class="lead">%s</p>'
                '<div class="hero-actions"><a class="button button-primary" href="%slien-he/">Gửi RFQ Endress+Hauser</a>'
                '%s</div></div></section>' % (
                img, up, g.e(g.SITE), up, g.e(m.get('primary_keyword','')),
                g.e('Kiến thức đo lường'), g.e(m.get('primary_keyword','')),
                g.e(m.get('title','')), g.e(desc), up,
                ('<a class="button button-secondary" href="%s%s/">Xem %s</a>' % (up, parent['slug'], g.e(parent['name']))) if parent else ''))

    # khoi anh + lien ket noi bo
    figs = ''
    if p:
        sides = ''.join(
            '<figure class="article-side-figure %s"><div class="article-image-stage">'
            '<img src="%sassets/products/%s" alt="%s — %s" loading="lazy"></div>'
            '<figcaption><strong>%s</strong>%s</figcaption></figure>' % (
                x['tone'], up, x['img'], g.e(x['title']), g.e(m.get('title','')), g.e(x['title']), g.e(x['category']))
            for x in ps['rel_products'][:2])
        figs = ('<div class="article-visual-pack">'
                '<figure class="article-featured-image %s"><div class="article-image-stage">'
                '<img src="%sassets/products/%s" alt="%s" width="640" height="640" loading="lazy"></div>'
                '<figcaption><strong>Ảnh chính: %s</strong>%s</figcaption></figure>'
                '<div class="article-support-images">%s</div></div>' % (
                p['tone'], up, p['img'], g.e(m.get('title','')), g.e(p['title']), g.e(p['category']), sides))

    links_cols = []
    if p:
        links_cols.append('<div><strong>Trang sản phẩm</strong><ul><li><a href="%s%s">%s</a></li></ul></div>'
                          % (up, p['url'], g.e(p['title'])))
    if parent:
        links_cols.append('<div><strong>Danh mục kỹ thuật</strong><ul><li><a href="%s%s/">%s</a></li>'
                          '<li><a href="%s%s/">%s</a></li></ul></div>'
                          % (up, parent['slug'], g.e(parent['name']),
                             up, byslug[p['main']]['slug'], g.e(byslug[p['main']]['name'])))
    if ps['rel_products']:
        links_cols.append('<div><strong>Model nên so sánh</strong><ul>%s</ul></div>'
                          % ''.join('<li><a href="%s%s">%s</a></li>' % (up, x['url'], g.e(x['title']))
                                    for x in ps['rel_products']))
    link_block = ('<div class="article-insight"><h2>Liên kết nên mở tiếp</h2><div class="insight-grid">%s</div></div>'
                  % ''.join(links_cols)) if links_cols else ''

    intro = ('<p>Fast Group Engineering cung cấp <strong>%s</strong> Endress+Hauser chính hãng tại Việt Nam — '
             'đầy đủ chứng từ nhập khẩu, CO/CQ và bảo hành chính hãng.</p>' % (
             g.e(m.get('primary_keyword','')),))

    cta = ('<h2>Nhận báo giá Endress+Hauser chính hãng</h2>'
           '<p>Gửi mã model, điều kiện quá trình, kết nối và yêu cầu chứng nhận qua email '
           '<a href="mailto:%s">%s</a> hoặc Zalo/điện thoại <a href="tel:%s">%s</a>. '
           'Hoặc <a href="%slien-he/">gửi RFQ qua biểu mẫu</a> và '
           '<a href="%stim-kiem/">tra mã model</a> trực tiếp trên trang.</p>' % (
           g.EMAIL, g.EMAIL, g.PHONE, g.PHONE_TXT, up, up))

    diagram = D.diagram_for(p) if p else ''
    body.append('<section class="section"><div class="container"><article class="article-body">%s%s%s%s%s%s</article></div></section>'
                % (intro, figs, diagram, link_block, g.md(ps['body']), cta))

    # bai lien quan
    others = [x for x in all_posts if x['slug'] != slug and x['product'] is not None and p is not None
              and x['product']['catalog'] == p['catalog']][:3]
    if others:
        cards = ''.join('<article class="card"><div class="product-meta">%s</div><h3><a href="%sblog/%s/">%s</a></h3>'
                        '<p>%s</p></article>' % (g.e(x['kw']), up, x['slug'], g.e(x['meta'].get('title','')),
                                                 g.e(x['meta'].get('meta_description','')))
                        for x in others)
        body.append('<section class="section section-soft"><div class="container">'
                    '<div class="section-heading"><div class="kicker">Bài liên quan</div>'
                    '<h2>Cùng nhóm %s</h2></div><div class="grid grid-3">%s</div></div></section>'
                    % (g.e(p['catalog_vi']), cards))

    g.write(os.path.join(OUT, 'blog', slug, 'index.html'), page(hd, up, hubs, ''.join(body)))


def build_blog_index(hubs, byslug, posts):
    up = '../'
    canon = g.BASE + 'blog/'
    title = 'Kiến thức đo lường Endress+Hauser | Fast Group'
    desc = ('Tài liệu kỹ thuật về thiết bị đo mức, đo áp suất, công tắc báo mức và đo nhiệt độ Endress+Hauser: '
            'nguyên lý đo, tiêu chí chọn cấu hình và lưu ý lắp đặt cho từng dòng thiết bị.')
    ld = {"@context":"https://schema.org","@type":"Blog","name":"Kiến thức đo lường Endress+Hauser",
          "url":canon,"inLanguage":"vi",
          "publisher":{"@type":"Organization","name":g.OWNER},
          "blogPost":[{"@type":"BlogPosting","headline":x['meta'].get('title',''),
                       "url":g.BASE+'blog/%s/'%x['slug']} for x in posts]}
    hd = g.head(title, desc, canon, up, extra_ld=[g.bc_ld([(g.SITE, g.BASE), ('Kiến thức đo lường', canon)]), ld])

    groups = {}
    for x in posts:
        k = x['product']['catalog_vi'] if x['product'] else 'Khác'
        groups.setdefault(k, []).append(x)
    blocks = []
    for k in ['Đo mức liên tục', 'Đo áp suất', 'Công tắc báo mức', 'Đo nhiệt độ']:
        if k not in groups:
            continue
        cards = ''.join(
            '<article class="card article-card"><div class="article-media">'
            '<img src="%sassets/products/%s" alt="%s" loading="lazy"></div>'
            '<div class="article-body"><div class="product-meta">%s</div>'
            '<h3><a href="%sblog/%s/">%s</a></h3><p>%s</p>'
            '<p class="meta-line">Model: %s</p></div></article>' % (
                up, x['product']['img'], g.e(x['meta'].get('title','')), g.e(x['kw']),
                up, x['slug'], g.e(x['meta'].get('title','')),
                g.e(x['meta'].get('meta_description','')), g.e(x['model']))
            for x in groups[k])
        blocks.append('<div class="section-heading" style="margin:38px 0 18px"><h2 style="font-size:1.5rem">%s '
                      '<span style="color:var(--muted);font-weight:600">· %d bài</span></h2></div>'
                      '<div class="article-list">%s</div>' % (g.e(k), len(groups[k]), cards))

    body = [g.breadcrumb_bar(up, [('', 'Trang chủ'), (None, 'Kiến thức đo lường')]),
            '<section class="page-hero category-hero" style="--page-image:url(\'/endress-hauser-viet-nam/assets/hero/eh-fmr51.png\')">'
            '<div class="container page-hero-inner"><div class="eyebrow">Kiến thức đo lường</div>'
            '<h1>Kiến thức đo lường Endress+Hauser</h1>'
            '<p class="lead">%s</p></div></section>' % g.e(desc),
            '<section class="section"><div class="container">%s</div></section>' % ''.join(blocks)]
    g.write(os.path.join(OUT, 'blog', 'index.html'), page(hd, up, hubs, ''.join(body)))

# ---------------------------------------------------------------- home
HOME_FAQ = [
    ('Fast Group có phải nhà cung cấp Endress+Hauser chính hãng tại Việt Nam không?',
     'Fast Group Engineering cung cấp thiết bị Endress+Hauser chính hãng cho nhà máy, nhà thầu EPC và đơn vị tích hợp hệ thống '
     'tại Việt Nam, kèm đầy đủ chứng từ nhập khẩu và CO/CQ theo từng đơn hàng.'),
    ('Thiết bị có đầy đủ chứng từ CO/CQ và bảo hành chính hãng không?',
     'Có. Mỗi lô hàng đi kèm bộ chứng từ nhập khẩu, Giấy chứng nhận xuất xứ (CO) và Chứng nhận chất lượng (CQ) của nhà sản xuất, '
     'cùng bảo hành chính hãng và hồ sơ kỹ thuật phục vụ nghiệm thu dự án.'),
    ('Fast Group hỗ trợ gì cho nhà máy và nhà thầu EPC?',
     'Tư vấn chọn nguyên lý đo và cấu hình theo điều kiện quá trình, đối chiếu Technical Information theo đúng mã đặt hàng, '
     'lập báo giá theo RFQ, và lo trọn khâu nhập khẩu, chứng từ cùng tiến độ giao hàng cho dự án.'),
    ('Cần cung cấp thông tin gì để được báo giá nhanh?',
     'Mã model hoặc bài toán đo, môi chất, nhiệt độ và áp suất làm việc, kết nối quá trình, tín hiệu / giao thức điều khiển '
     'và yêu cầu chứng nhận (Ex, SIL, CO/CQ). Đủ các thông tin này, báo giá được lập nhanh và chính xác.'),
]

def build_home(hubs, byslug, prods, posts):
    up = ''
    canon = g.BASE
    title = 'Endress+Hauser Việt Nam | Thiết bị đo mức, áp suất, nhiệt độ chính hãng'
    desc = ('Fast Group Engineering cung cấp thiết bị Endress+Hauser chính hãng tại Việt Nam: 160 model đo mức, đo áp suất, '
            'công tắc báo mức và đo nhiệt độ. Tra mã, xem thông số theo catalog, tư vấn cấu hình và gửi RFQ kèm CO/CQ.')
    site_ld = {"@context":"https://schema.org","@type":"WebSite","name":g.SITE,"url":canon,"inLanguage":"vi",
               "publisher":{"@type":"Organization","name":g.OWNER},
               "potentialAction":{"@type":"SearchAction",
                   "target":canon+"tim-kiem/?q={search_term_string}",
                   "query-input":"required name=search_term_string"}}
    mains = [x for x in hubs if x['kind'] == 'main']
    item_ld = {"@context":"https://schema.org","@type":"ItemList","name":"Danh mục Endress+Hauser",
               "numberOfItems":len(mains),
               "itemListElement":[{"@type":"ListItem","position":i+1,"url":g.BASE+x['slug']+'/',"name":x['name']}
                                  for i, x in enumerate(mains)]}
    hd = g.head(title, desc, canon, up,
                image=g.BASE+'assets/products/eh-fmr51.png',
                extra_ld=[site_ld, item_ld, g.faq_ld(HOME_FAQ)])

    cat_cards = ''.join(
        '<article class="card category-card %s"><a class="category-media" href="%s/">'
        '<img src="assets/products/%s" alt="%s Endress+Hauser" loading="lazy" /></a>'
        '<h3><a href="%s/">%s</a></h3><p>%s</p><p class="meta-line">%d model</p></article>' % (
            x['tone'], x['slug'], (([y for y in x['items'] if y['sku']==x.get('hero_sku')] or x['items'])[0])['img'], g.e(x['name']), x['slug'], g.e(x['name']),
            g.e(x['meta'].get('lead','')[:190] + '…'), len(x['items']))
        for x in mains)

    techs = [x for x in hubs if x['kind'] == 'tech']
    tech_links = ''.join('<a href="%s/">%s <span style="font-weight:600;color:var(--muted)">· %d model</span></a>'
                         % (x['slug'], g.e(x['name']), len(x['items'])) for x in techs)

    featured_skus = ['FMR20B / FMR30B', 'FMR51', 'FMP51', 'FMU30', 'PMP71B', 'PMD75B', 'FTL51', 'TMT82']
    idx = {p['sku']: p for p in prods}
    feat = [idx[s] for s in featured_skus if s in idx]
    if len(feat) < 8:
        feat += [p for p in prods if p not in feat][:8-len(feat)]

    top_posts = posts[:4]
    post_cards = ''.join(
        '<article class="card"><div class="product-meta">%s</div><h3><a href="blog/%s/">%s</a></h3><p>%s</p></article>'
        % (g.e(x['kw']), x['slug'], g.e(x['meta'].get('title','')), g.e(x['meta'].get('meta_description','')))
        for x in top_posts)

    body = []
    body.append(
        '<section class="hero" style="--hero-image:url(\'/endress-hauser-viet-nam/assets/hero/eh-fmr51.png\')">'
        '<div class="container hero-inner"><div class="hero-copy">'
        '<div class="eyebrow">%s · Cung cấp Endress+Hauser chính hãng tại Việt Nam</div>'
        '<h1>Endress+Hauser Việt Nam — thiết bị đo mức, áp suất, nhiệt độ cho nhà máy</h1>'
        '<p class="lead">Tra mã Endress+Hauser, so sánh model theo nguyên lý đo và điều kiện quá trình, xem thông số theo '
        'catalog chính thức rồi gửi RFQ. Fast Group hỗ trợ đối chiếu datasheet, chọn cấu hình, nhập khẩu và CO/CQ.</p>'
        '<form id="check-ma" class="search-panel" action="tim-kiem/" method="get" autocomplete="off">'
        '<input id="heroq" name="q" type="search" placeholder="Nhập mã model: FMR20B, PMP71B, FTL51, TMT82..." '
        'autocomplete="off" aria-label="Tìm mã Endress+Hauser" />'
        '<button class="button button-primary" type="submit">Tra mã</button>'
        '<div id="heroAc" class="hero-ac" role="listbox" aria-label="Gợi ý mã Endress+Hauser"></div>'
        '<div class="search-note">Tìm theo mã model, dòng sản phẩm, nguyên lý đo hoặc nhóm ứng dụng trong 160 model Endress+Hauser.</div>'
        '</form>'
        '<div class="hero-actions"><a class="button button-primary" href="lien-he/">Gửi RFQ Endress+Hauser</a>'
        '<a class="button button-secondary" href="#danh-muc">Xem danh mục</a></div>'
        '</div></div></section>' % g.e(g.OWNER))

    body.append('<section class="metric-strip"><div class="container metrics">'
                '<div class="metric"><strong>100% chính hãng</strong><span>Nhập khẩu trực tiếp, truy xuất nguồn gốc</span></div>'
                '<div class="metric"><strong>Đầy đủ CO/CQ</strong><span>Chứng từ nhập khẩu theo từng lô hàng</span></div>'
                '<div class="metric"><strong>Bảo hành chính hãng</strong><span>Hỗ trợ kỹ thuật và hồ sơ nghiệm thu</span></div>'
                '<div class="metric"><strong>Báo giá theo RFQ</strong><span>Tư vấn cấu hình đúng mã đặt hàng</span></div>'
                '</div></section>')

    body.append('<section class="section" id="danh-muc"><div class="container">'
                '<div class="section-heading center"><div class="kicker">Danh mục Endress+Hauser</div>'
                '<h2>Bốn lĩnh vực đo lường quá trình</h2>'
                '<p>Đo mức, đo áp suất, công tắc báo mức và đo nhiệt độ — phân theo công nghệ đo để tra cứu đúng model và cấu hình.</p></div>'
                '<div class="grid grid-4">%s</div>'
                '<div class="section-heading" style="margin:44px 0 14px"><h2 style="font-size:1.4rem">Đi sâu theo công nghệ đo</h2></div>'
                '<div class="hub-grid">%s</div></div></section>' % (cat_cards, tech_links))

    body.append('<section class="section section-soft"><div class="container">'
                '<div class="section-heading"><div class="kicker">Model tiêu biểu</div>'
                '<h2>Những mã Endress+Hauser được hỏi nhiều nhất</h2>'
                '<p>Các dòng thiết bị đo lường quá trình thông dụng cho nhà máy dầu khí, hóa chất, thực phẩm và nước.</p></div>%s'
                '<p class="center" style="margin-top:26px"><a class="button button-secondary" href="san-pham/">'
                'Xem tất cả 160 model Endress+Hauser</a></p></div></section>' % R.product_grid(feat, up))

    body.append('<section class="section"><div class="container split"><div>'
                '<div class="section-heading"><div class="kicker">Cam kết của Fast Group</div>'
                '<h2>Hàng chính hãng, hồ sơ đầy đủ, hỗ trợ tận nơi</h2>'
                '<p>Fast Group Engineering là đối tác cung cấp Endress+Hauser cho nhà máy, nhà thầu EPC và đơn vị tích hợp '
                'hệ thống trên toàn quốc — từ tư vấn cấu hình đến giao hàng và hồ sơ nghiệm thu.</p></div>'
                '<ul class="check-list">'
                '<li>Thiết bị chính hãng 100%, nhập khẩu trực tiếp, truy xuất nguồn gốc rõ ràng.</li>'
                '<li>Đầy đủ chứng từ nhập khẩu, CO/CQ và bảo hành chính hãng theo từng lô.</li>'
                '<li>Tư vấn chọn nguyên lý đo và cấu hình theo điều kiện quá trình thực tế.</li>'
                '<li>Hỗ trợ kỹ thuật, đối chiếu datasheet và tiến độ giao hàng cho dự án.</li></ul></div>'
                '<aside class="quote-panel"><div class="kicker">RFQ Endress+Hauser</div>'
                '<h2>Gửi yêu cầu báo giá</h2><p>Càng đủ dữ liệu kỹ thuật, báo giá càng nhanh và càng ít phải hỏi lại.</p>'
                '<ul class="quote-list"><li>Mã model hoặc mô tả bài toán đo</li>'
                '<li>Môi chất, nhiệt độ, áp suất làm việc</li>'
                '<li>Kết nối quá trình sẵn có</li>'
                '<li>Tín hiệu / giao thức của hệ điều khiển</li>'
                '<li>Yêu cầu chứng nhận, CO/CQ</li></ul>'
                '<a class="button button-secondary" href="lien-he/">Gửi RFQ</a></aside></div></section>')

    body.append('<section class="section section-soft"><div class="container">'
                '<div class="section-heading"><div class="kicker">Kiến thức đo lường</div>'
                '<h2>Tài liệu kỹ thuật theo từng dòng thiết bị</h2>'
                '<p>Nguyên lý đo, tiêu chí chọn cấu hình và lưu ý lắp đặt cho từng dòng Endress+Hauser.</p>'
                '</div><div class="grid grid-4">%s</div>'
                '<p class="center" style="margin-top:26px"><a class="button button-secondary" href="blog/">'
                'Xem tất cả bài kiến thức đo lường</a></p></div></section>' % post_cards)

    body.append('<section class="section"><div class="container">'
                '<div class="section-heading"><div class="kicker">Câu hỏi thường gặp</div>'
                '<h2>Mua Endress+Hauser chính hãng tại Việt Nam</h2></div>%s</div></section>' % g.faq_html(HOME_FAQ))

    g.write(os.path.join(OUT, 'index.html'), page(hd, up, hubs, ''.join(body)))


def build_products_index(hubs, byslug, prods):
    up = '../'
    canon = g.BASE + 'san-pham/'
    title = 'Tất cả sản phẩm Endress+Hauser | 160 model — Fast Group'
    desc = ('Danh sách đầy đủ 160 model Endress+Hauser: đo mức, đo áp suất, công tắc báo mức và đo nhiệt độ. '
            'Xem nguyên lý, dải đo, nhiệt độ quá trình và tín hiệu ra của từng model, gửi RFQ theo mã.')
    ld = {"@context":"https://schema.org","@type":"ItemList","name":"Sản phẩm Endress+Hauser",
          "numberOfItems":len(prods),
          "itemListElement":[{"@type":"ListItem","position":i+1,"url":p['abs'],"name":p['title']}
                             for i, p in enumerate(prods)]}
    hd = g.head(title, desc, canon, up,
                extra_ld=[g.bc_ld([(g.SITE, g.BASE), ('Tất cả sản phẩm', canon)]), ld])
    blocks = []
    for h in [x for x in hubs if x['kind'] == 'main']:
        blocks.append('<div class="section-heading" style="margin:38px 0 16px">'
                      '<h2 style="font-size:1.55rem"><a href="%s%s/">%s</a> '
                      '<span style="color:var(--muted);font-weight:600">· %d model</span></h2></div>%s'
                      % (up, h['slug'], g.e(h['name']), len(h['items']), R.product_table(h['items'], up)))
    body = [g.breadcrumb_bar(up, [('', 'Trang chủ'), (None, 'Tất cả sản phẩm')]),
            '<section class="page-hero category-hero" style="--page-image:url(\'/endress-hauser-viet-nam/assets/hero/eh-pmp71b.png\')">'
            '<div class="container page-hero-inner"><div class="eyebrow">Danh mục đầy đủ</div>'
            '<h1>160 model Endress+Hauser trong catalog</h1><p class="lead">%s</p>'
            '<div class="hero-actions"><a class="button button-primary" href="%stim-kiem/">Tra mã nhanh</a>'
            '<a class="button button-secondary" href="%slien-he/">Gửi RFQ</a></div></div></section>' % (g.e(desc), up, up),
            '<section class="section"><div class="container">%s</div></section>' % ''.join(blocks)]
    g.write(os.path.join(OUT, 'san-pham', 'index.html'), page(hd, up, hubs, ''.join(body)))

# ---------------------------------------------------------------- trang phu
def build_search(hubs, byslug, prods):
    up = '../'
    canon = g.BASE + 'tim-kiem/'
    title = 'Tra mã Endress+Hauser | Tìm model theo part number — Fast Group'
    desc = ('Tra mã Endress+Hauser theo part number hoặc theo nhu cầu đo: nhập FMR20B, PMP71B, FTL51, TMT82 hoặc cụm từ như '
            'radar đo mức, chênh áp, công tắc mức, nhiệt kế vệ sinh.')
    hd = g.head(title, desc, canon, up, extra_ld=[g.bc_ld([(g.SITE, g.BASE), ('Tra mã', canon)])])
    body = [g.breadcrumb_bar(up, [('', 'Trang chủ'), (None, 'Tra mã')]),
            '<section class="page-hero category-hero" style="--page-image:url(\'/endress-hauser-viet-nam/assets/hero/eh-ftl51.png\')">'
            '<div class="container page-hero-inner"><div class="eyebrow">Tra mã Endress+Hauser</div>'
            '<h1>Tìm model Endress+Hauser theo mã hoặc theo nhu cầu đo</h1><p class="lead">%s</p></div></section>' % g.e(desc),
            '<section class="section"><div class="container"><div class="search-page">'
            '<input id="siteSearch" type="search" placeholder="Tìm FMR20B, PMP71B, FTL51, TMT82, radar đo mức..." '
            'aria-label="Tìm sản phẩm Endress+Hauser">'
            '<div id="searchResults" class="article-list"></div></div></div></section>'
            '<script>window.EH_SEARCH_PAGE=true;</script>']
    g.write(os.path.join(OUT, 'tim-kiem', 'index.html'), page(hd, up, hubs, ''.join(body)))


def build_contact(hubs):
    up = '../'
    canon = g.BASE + 'lien-he/'
    title = 'Gửi RFQ Endress+Hauser | Báo giá thiết bị chính hãng — Fast Group'
    desc = ('Gửi yêu cầu báo giá thiết bị Endress+Hauser chính hãng tại Việt Nam. Cung cấp mã model, môi chất, nhiệt độ, '
            'áp suất, kết nối quá trình và yêu cầu chứng nhận để nhận tư vấn cấu hình và giá nhanh.')
    ct_ld = {"@context":"https://schema.org","@type":"ContactPage","name":title,"url":canon,
             "mainEntity":{"@type":"Organization","name":g.OWNER,"email":g.EMAIL,"telephone":g.PHONE,
                           "url":g.ROOT,
                           "address":{"@type":"PostalAddress","streetAddress":g.ADDR,
                                      "addressLocality":"Ho Chi Minh City","addressCountry":"VN"}}}
    hd = g.head(title, desc, canon, up, extra_ld=[g.bc_ld([(g.SITE, g.BASE), ('Liên hệ', canon)]), ct_ld])
    body = [g.breadcrumb_bar(up, [('', 'Trang chủ'), (None, 'Liên hệ')]),
            '<section class="page-hero category-hero" style="--page-image:url(\'/endress-hauser-viet-nam/assets/hero/eh-pmd75b.png\')">'
            '<div class="container page-hero-inner"><div class="eyebrow">RFQ Endress+Hauser</div>'
            '<h1>Gửi yêu cầu báo giá thiết bị Endress+Hauser chính hãng</h1>'
            '<p class="lead">Càng đủ dữ liệu kỹ thuật, báo giá càng nhanh: mã model, môi chất, nhiệt độ và áp suất làm việc, '
            'kết nối quá trình, tín hiệu ra và yêu cầu chứng nhận.</p></div></section>',
            '<section class="section"><div class="container contact-layout">'
            '<div class="form-panel"><h2>Thông tin nên gửi trong RFQ</h2><div class="form-grid">'
            '<div class="field"><label>Mã model</label><input id="rfqModel" value="FMR20B / PMP71B / FTL51 / TMT82..." readonly></div>'
            '<div class="field"><label>Nhóm đo</label><select>'
            '<option>Đo mức liên tục</option><option>Đo áp suất & chênh áp</option>'
            '<option>Công tắc báo mức</option><option>Đo nhiệt độ</option></select></div>'
            '<div class="field"><label>Điều kiện quá trình</label><input value="Môi chất, nhiệt độ, áp suất làm việc" readonly></div>'
            '<div class="field"><label>Kết nối & tín hiệu</label><input value="Ren/mặt bích; 4-20mA, HART, PROFIBUS PA..." readonly></div>'
            '<div class="field full"><label>Nội dung RFQ mẫu</label>'
            '<textarea readonly>Kính gửi Fast Group, vui lòng báo giá Endress+Hauser [mã model], số lượng [..]. '
            'Điều kiện quá trình: môi chất [..], nhiệt độ [..], áp suất [..]. Kết nối quá trình [..], tín hiệu ra [..]. '
            'Yêu cầu chứng nhận [ATEX/IECEx nếu có], CO/CQ và lead time giao tại [địa điểm].</textarea></div>'
            '</div><div class="form-actions">'
            '<a class="button button-primary" href="mailto:%s?subject=RFQ%%20Endress%%2BHauser">Gửi email RFQ</a>'
            '<a class="button button-secondary" href="tel:%s">Gọi/Zalo %s</a></div></div>'
            '<aside class="contact-stack">'
            '<div class="contact-card"><h3>Email</h3><p><a href="mailto:%s">%s</a></p></div>'
            '<div class="contact-card"><h3>Điện thoại / Zalo</h3><p><a href="tel:%s">%s</a></p></div>'
            '<div class="contact-card"><h3>Trụ sở</h3><p>%s</p></div>'
            '<div class="contact-card"><h3>Chưa có mã model?</h3><p>Gửi ảnh nhãn thiết bị đang dùng hoặc mô tả bài toán đo '
            '(môi chất, kích thước bồn, điều kiện vận hành) để Fast Group đề xuất model tương đương.</p></div>'
            '</aside></div></section>' % (g.EMAIL, g.PHONE, g.PHONE_TXT, g.EMAIL, g.EMAIL, g.PHONE, g.PHONE_TXT, g.e(g.ADDR)),
            '<script>(function(){var m=new URLSearchParams(location.search).get("model");'
            'if(m){var i=document.getElementById("rfqModel");if(i){i.value=m;}}})();</script>']
    g.write(os.path.join(OUT, 'lien-he', 'index.html'), page(hd, up, hubs, ''.join(body)))


def build_about(hubs):
    up = '../'
    canon = g.BASE + 've-chung-toi/'
    title = 'Về Fast Group Engineering | Phân phối Endress+Hauser chính hãng tại Việt Nam'
    desc = ('Fast Group Engineering — nhà phân phối thiết bị công nghiệp chính hãng tại Việt Nam, làm việc trực tiếp với nguồn cung. '
            'Với Endress+Hauser: đối chiếu mã đặt hàng, tư vấn cấu hình theo điều kiện quá trình, nhập khẩu và CO/CQ.')
    hd = g.head(title, desc, canon, up, extra_ld=[g.bc_ld([(g.SITE, g.BASE), ('Về chúng tôi', canon)])])
    body = [g.breadcrumb_bar(up, [('', 'Trang chủ'), (None, 'Về chúng tôi')]),
            '<section class="page-hero category-hero" style="--page-image:url(\'/endress-hauser-viet-nam/assets/hero/eh-tmt82.png\')">'
            '<div class="container page-hero-inner"><div class="eyebrow">Fast Group Engineering</div>'
            '<h1>Nhà phân phối làm việc trực tiếp với nguồn cung</h1>'
            '<p class="lead">Đối tác cung cấp Endress+Hauser chính hãng cho nhà máy, nhà thầu EPC và đơn vị tích hợp hệ thống '
            'tại Việt Nam — làm việc trực tiếp với nguồn cung, đầy đủ chứng từ nhập khẩu và CO/CQ.</p></div></section>',

            '<section class="section"><div class="container split"><div><article class="article-body">'
            '<h2>Fast Group Engineering</h2>'
            '<p>Thành lập năm 2019, Công ty TNHH Fast Group (MST %(mst)s) là nhà phân phối thiết bị và vật tư công nghiệp chính hãng '
            'tại Việt Nam, phục vụ nhà máy sản xuất, nhà thầu EPC, đơn vị tích hợp hệ thống và các dự án dầu khí, hóa chất, năng lượng, '
            'nước và thực phẩm.</p>'
            '<p>Điều tạo nên khác biệt không nằm ở độ dài danh mục — mà ở <strong>quan hệ làm việc trực tiếp với nguồn cung</strong>. '
            'Nhờ đó chúng tôi chủ động được bốn thứ mà khách hàng công nghiệp thực sự quan tâm: tính chính hãng của từng lô, giá, '
            'thời gian giao, và bộ chứng từ đi kèm.</p>'
            '<p>Trụ sở đặt tại TP. Hồ Chí Minh, văn phòng tại Vũng Tàu — trung tâm ngành dầu khí Việt Nam — và hiện diện tại Singapore. '
            'Vị trí này giúp chúng tôi kết nối nguồn cung quốc tế với tiến độ thực tế của nhà máy và dự án trong nước.</p>'

            '<h2>Vì sao điều đó quan trọng với thiết bị đo</h2>'
            '<p>Thiết bị đo lường quá trình không phải hàng mua theo tên model. Cùng một mã Endress+Hauser có thể ra hàng chục cấu hình '
            'khác nhau tùy kết nối quá trình, vật liệu tiếp xúc, dải đo, giao thức truyền thông và chứng nhận phòng nổ. Chọn sai một '
            'trong số đó thì thiết bị vẫn về đúng hạn nhưng không lắp được, hoặc lắp được mà không qua nghiệm thu.</p>'
            '<p>Vì vậy quy trình của chúng tôi bắt đầu từ việc <strong>xác nhận đúng cấu hình trước khi báo giá</strong>, chứ không phải '
            'xử lý sau khi hàng đã về. Với mỗi yêu cầu, chúng tôi đối chiếu Technical Information theo đúng mã đặt hàng, kiểm tra điều '
            'kiện quá trình thực tế mà khách hàng mô tả, và nêu rõ nếu thấy model được hỏi không phù hợp — kể cả khi điều đó dẫn tới '
            'một model rẻ hơn.</p>'

            '<h2>Fast Group đảm nhận</h2>'
            '<ul>'
            '<li>Đối chiếu datasheet và xác nhận cấu hình theo đúng mã đặt hàng</li>'
            '<li>Tư vấn chọn nguyên lý đo và model theo điều kiện quá trình thực tế</li>'
            '<li>Kiểm tra yêu cầu chứng nhận phòng nổ, an toàn chức năng và chứng nhận vệ sinh</li>'
            '<li>Nhập khẩu, thông quan, CO/CQ và hồ sơ kỹ thuật theo yêu cầu dự án</li>'
            '<li>Hỗ trợ vendor, đại lý và nhà thầu tiếp cận hàng chính hãng cùng bộ tài liệu đầy đủ</li>'
            '<li>Hỗ trợ kỹ thuật trước và sau bán hàng</li>'
            '</ul>'
            '</article></div>'

            '<aside class="quote-panel"><div class="kicker">Liên hệ</div><h2>Làm việc với Fast Group</h2>'
            '<ul class="quote-list"><li>Email: %(mail)s</li><li>Điện thoại / Zalo: %(ph)s</li>'
            '<li>Trụ sở: %(addr)s</li><li>VP Vũng Tàu: %(addr2)s</li>'
            '<li>VP Singapore: Blk 502 Tampines Central 1, #08-295</li></ul>'
            '<a class="button button-secondary" href="%(up)slien-he/">Gửi RFQ</a></aside></div></section>'
            % dict(mst=g.MST, mail=g.EMAIL, ph=g.PHONE_TXT, addr=g.e(g.ADDR), addr2=g.e(g.ADDR2), up=up)]
    g.write(os.path.join(OUT, 've-chung-toi', 'index.html'), page(hd, up, hubs, ''.join(body)))


# ---------------------------------------------------------------- assets & sitemap
def build_search_index(prods, hubs, posts):
    rows = []
    for p in prods:
        desc = ' · '.join(x for x in [R.clean(p.get('short_desc')), R.clean(p.get('measuring_principle')),
                                      R.clean(p.get('measuring_range')), R.clean(p.get('output_comm')),
                                      R.clean(p.get('key_features'))] if x)
        rows.append(dict(type='Sản phẩm', code=p['sku'], title=p['title'], desc=desc or p['category'],
                         url='../' + p['url'], category=p['category']))
    for h in hubs:
        rows.append(dict(type='Danh mục', code=h['name'], title=h['name'],
                         desc=h['meta'].get('lead', ''), url='../%s/' % h['slug'], category='Danh mục kỹ thuật'))
    for ps in posts:
        rows.append(dict(type='Bài viết', code=ps['model'], title=ps['meta'].get('title', ''),
                         desc=ps['meta'].get('meta_description', ''), url='../blog/%s/' % ps['slug'],
                         category=ps['meta'].get('category', 'Kiến thức đo lường')))
    js = 'window.EH_SEARCH_INDEX=' + json.dumps(rows, ensure_ascii=False, separators=(',', ':')) + ';'
    g.write(os.path.join(OUT, 'assets', 'search-index.js'), js)
    return len(rows)


def build_sitemaps(prods, hubs, posts):
    def urlset(urls):
        out = ['<?xml version="1.0" encoding="UTF-8"?>',
               '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
        for loc, pri in urls:
            out.append('  <url>\n    <loc>%s</loc>\n    <lastmod>%s</lastmod>\n    <priority>%s</priority>\n  </url>'
                       % (loc, g.BUILD, pri))
        out.append('</urlset>')
        return '\n'.join(out)

    pages = [(g.BASE, '1.00'), (g.BASE + 'san-pham/', '0.90'),
             (g.BASE + 'tim-kiem/', '0.70'), (g.BASE + 'lien-he/', '0.80'),
             (g.BASE + 've-chung-toi/', '0.60'), (g.BASE + 'blog/', '0.80')]
    for h in hubs:
        pages.append((g.BASE + h['slug'] + '/', '0.88' if h['kind'] == 'main' else '0.85'))
    g.write(os.path.join(OUT, 'sitemap-pages.xml'), urlset(pages))
    g.write(os.path.join(OUT, 'sitemap-products.xml'), urlset([(p['abs'], '0.75') for p in prods]))
    g.write(os.path.join(OUT, 'sitemap-blog.xml'),
            urlset([(g.BASE + 'blog/%s/' % x['slug'], '0.70') for x in posts]))
    idx = ['<?xml version="1.0" encoding="UTF-8"?>', '<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for n in ('sitemap-pages.xml', 'sitemap-products.xml', 'sitemap-blog.xml'):
        idx.append('  <sitemap><loc>%s%s</loc><lastmod>%s</lastmod></sitemap>' % (g.BASE, n, g.BUILD))
    idx.append('</sitemapindex>')
    g.write(os.path.join(OUT, 'sitemap_index.xml'), '\n'.join(idx))
    g.write(os.path.join(OUT, 'robots.txt'),
            'User-agent: *\nAllow: /\n\nSitemap: %ssitemap_index.xml\n' % g.BASE)
    return len(pages) + len(prods) + len(posts)
