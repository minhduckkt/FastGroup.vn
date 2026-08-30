# -*- coding: utf-8 -*-
"""Thu vien dung chung cho bo sinh site Endress+Hauser Viet Nam."""
import re, html, json, os

BASE   = 'https://fastgroup.vn/endress-hauser-viet-nam/'
ROOT   = 'https://fastgroup.vn/'
SITE   = 'Endress+Hauser Việt Nam'
OWNER  = 'Fast Group Engineering'
EMAIL  = 'minhduc@fastgroup.vn'
PHONE  = '+84938888958'
PHONE_TXT = '(+84) 938 888 958'
ADDR   = '150/41 Nguyen Cu Trinh Street, Cau Ong Lanh Ward, District 1, Ho Chi Minh City, Vietnam'
ADDR2  = '51 Le Van Loc Street, Vung Tau City, Vietnam'
MST    = '0315555189'
THEME  = '#00697c'
BUILD  = '2026-08-30'

def e(s):
    return html.escape(str(s or ''), quote=True)

def jsonld(obj):
    return '<script type="application/ld+json">%s</script>' % json.dumps(obj, ensure_ascii=False, separators=(',', ':'))

def slugify(s):
    s = str(s or '').lower()
    tr = {'à':'a','á':'a','ả':'a','ã':'a','ạ':'a','ă':'a','ằ':'a','ắ':'a','ẳ':'a','ẵ':'a','ặ':'a',
          'â':'a','ầ':'a','ấ':'a','ẩ':'a','ẫ':'a','ậ':'a','đ':'d','è':'e','é':'e','ẻ':'e','ẽ':'e',
          'ẹ':'e','ê':'e','ề':'e','ế':'e','ể':'e','ễ':'e','ệ':'e','ì':'i','í':'i','ỉ':'i','ĩ':'i',
          'ị':'i','ò':'o','ó':'o','ỏ':'o','õ':'o','ọ':'o','ô':'o','ồ':'o','ố':'o','ổ':'o','ỗ':'o',
          'ộ':'o','ơ':'o','ờ':'o','ớ':'o','ở':'o','ỡ':'o','ợ':'o','ù':'u','ú':'u','ủ':'u','ũ':'u',
          'ụ':'u','ư':'u','ừ':'u','ứ':'u','ử':'u','ữ':'u','ự':'u','ỳ':'y','ý':'y','ỷ':'y','ỹ':'y','ỵ':'y'}
    s = ''.join(tr.get(c, c) for c in s)
    s = re.sub(r'[^a-z0-9]+', '-', s).strip('-')
    return re.sub(r'-+', '-', s)

# ---------------------------------------------------------------- markdown
_INLINE = [
    (re.compile(r'\*\*(.+?)\*\*'), r'<strong>\1</strong>'),
    (re.compile(r'(?<![\w*])\*([^*\n]+?)\*(?![\w*])'), r'<em>\1</em>'),
    (re.compile(r'`([^`]+?)`'), r'<code>\1</code>'),
]

def inline(t):
    t = html.escape(t, quote=False)
    t = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', lambda m: '<a href="%s">%s</a>' % (html.escape(m.group(2), True), m.group(1)), t)
    for rx, rep in _INLINE:
        t = rx.sub(rep, t)
    return t

def md(text):
    """Markdown rut gon -> HTML: heading, p, ul/ol, table, blockquote, hr."""
    out, lines, i = [], text.split('\n'), 0
    while i < len(lines):
        ln = lines[i]
        s = ln.strip()
        if not s:
            i += 1; continue
        m = re.match(r'^(#{1,4})\s+(.*)$', s)
        if m:
            lv = len(m.group(1))
            out.append('<h%d>%s</h%d>' % (lv, inline(m.group(2)), lv)); i += 1; continue
        if s.startswith('|') and i + 1 < len(lines) and re.match(r'^\|[\s:|-]+\|$', lines[i+1].strip()):
            hdr = [c.strip() for c in s.strip('|').split('|')]
            i += 2; body = []
            while i < len(lines) and lines[i].strip().startswith('|'):
                body.append([c.strip() for c in lines[i].strip().strip('|').split('|')]); i += 1
            t = ['<div class="md-table-wrap"><table class="md-table"><thead><tr>']
            t += ['<th>%s</th>' % inline(c) for c in hdr]
            t.append('</tr></thead><tbody>')
            for r in body:
                t.append('<tr>' + ''.join('<td>%s</td>' % inline(c) for c in r) + '</tr>')
            t.append('</tbody></table></div>')
            out.append(''.join(t)); continue
        if re.match(r'^[-*]\s+', s):
            items = []
            while i < len(lines) and re.match(r'^[-*]\s+', lines[i].strip()):
                items.append(re.sub(r'^[-*]\s+', '', lines[i].strip())); i += 1
            out.append('<ul>' + ''.join('<li>%s</li>' % inline(x) for x in items) + '</ul>'); continue
        if re.match(r'^\d+\.\s+', s):
            items = []
            while i < len(lines) and re.match(r'^\d+\.\s+', lines[i].strip()):
                items.append(re.sub(r'^\d+\.\s+', '', lines[i].strip())); i += 1
            out.append('<ol>' + ''.join('<li>%s</li>' % inline(x) for x in items) + '</ol>'); continue
        if s.startswith('>'):
            buf = []
            while i < len(lines) and lines[i].strip().startswith('>'):
                buf.append(lines[i].strip().lstrip('>').strip()); i += 1
            out.append('<div class="article-insight caution"><p>%s</p></div>' % inline(' '.join(buf))); continue
        if re.match(r'^-{3,}$', s):
            i += 1; continue
        buf = []
        while i < len(lines) and lines[i].strip() and not re.match(r'^(#{1,4}\s|[-*]\s|\d+\.\s|\||>|-{3,}$)', lines[i].strip()):
            buf.append(lines[i].strip()); i += 1
        if buf:
            out.append('<p>%s</p>' % inline(' '.join(buf)))
    return '\n'.join(out)

def front_matter(raw):
    """Tach YAML front matter don gian -> (dict, body)."""
    if not raw.startswith('---'):
        return {}, raw
    end = raw.index('\n---', 3)
    head, body = raw[3:end], raw[end+4:]
    meta = {}
    for line in head.split('\n'):
        line = line.strip()
        if not line or ':' not in line:
            continue
        k, v = line.split(':', 1)
        v = v.strip()
        if v.startswith('[') and v.endswith(']'):
            v = [x.strip().strip('"\'') for x in v[1:-1].split(',') if x.strip()]
        else:
            v = v.strip('"\'')
        meta[k.strip()] = v
    return meta, body.strip()

# ---------------------------------------------------------------- chrome
ORG_LD = {"@context":"https://schema.org","@type":"Organization","name":OWNER,"url":ROOT,
          "logo":ROOT+"img/logo.png","email":EMAIL,"telephone":PHONE,
          "address":{"@type":"PostalAddress","streetAddress":ADDR,
                     "addressLocality":"Ho Chi Minh City","addressCountry":"VN"}}

def nav_items(hubs):
    """[(href_rel, label)] cho dropdown San pham."""
    return [(h['slug'] + '/', h['nav_label']) for h in hubs]

def head(title, desc, canon, up, image=None, extra_ld=(), og_type='website'):
    img = image or (BASE + 'assets/images/endress-hauser-og.png')
    L = ['<!doctype html>', '<html lang="vi"><head>',
         '<meta charset="utf-8" />',
         '<meta name="viewport" content="width=device-width, initial-scale=1" />',
         '<title>%s</title>' % e(title),
         '<meta name="description" content="%s" />' % e(desc),
         '<meta name="robots" content="index,follow" />',
         '<meta name="theme-color" content="%s" />' % THEME,
         '<link rel="canonical" href="%s" />' % e(canon),
         '<meta property="og:title" content="%s" />' % e(title),
         '<meta property="og:description" content="%s" />' % e(desc),
         '<meta property="og:type" content="%s" />' % og_type,
         '<meta property="og:url" content="%s" />' % e(canon),
         '<meta property="og:locale" content="vi_VN" />',
         '<meta property="og:image" content="%s" />' % e(img),
         '<meta name="twitter:card" content="summary_large_image" />',
         '<meta name="twitter:title" content="%s" />' % e(title),
         '<meta name="twitter:description" content="%s" />' % e(desc),
         '<meta name="twitter:image" content="%s" />' % e(img),
         '<link rel="preconnect" href="https://fonts.googleapis.com" />',
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />',
         '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@400;500;600;700&display=swap" />',
         '<link rel="icon" href="%simg/favicon.ico" />' % ROOT,
         '<link rel="stylesheet" href="%sassets/site.css?v=%s" />' % (up, BUILD),
         jsonld(ORG_LD)]
    for o in extra_ld:
        L.append(jsonld(o))
    L.append('</head><body>')
    return '\n'.join(L)

def header(up, hubs):
    dd = ''.join('<a href="%s%s">%s</a>' % (up, h, e(lb)) for h, lb in nav_items(hubs))
    dd += '<a href="%ssan-pham/">Tất cả sản phẩm Endress+Hauser</a>' % up
    return ('<header class="site-header"><div class="header-inner">'
            '<a class="brand" href="%(up)s" aria-label="%(site)s"><img class="brand-logo" src="%(up)sassets/brand/eh-logo.png" alt="Endress+Hauser" width="68" height="38" />'
            '<span><span class="brand-name">%(site)s</span><span class="brand-sub">%(own)s</span></span></a>'
            '<nav class="nav" aria-label="Điều hướng chính">'
            '<a href="%(up)s">Trang chủ</a>'
            '<details class="nav-dropdown"><summary>Sản phẩm</summary><div class="nav-dropdown-panel">%(dd)s</div></details>'
            '<a href="%(up)stim-kiem/">Tra mã</a>'
            '<a href="%(up)sblog/">Kiến thức đo lường</a>'
            '<a href="%(up)sve-chung-toi/">Về chúng tôi</a>'
            '<a href="%(up)slien-he/">Liên hệ</a>'
            '<a class="nav-cta" href="%(up)slien-he/">Gửi RFQ</a>'
            '</nav></div></header>') % dict(up=up, site=e(SITE), own=e(OWNER), dd=dd)

def footer(up, hubs):
    cats = ''.join('<a href="%s%s">%s</a>' % (up, h, e(lb)) for h, lb in nav_items(hubs)[:6])
    cats += '<a href="%ssan-pham/">Tất cả mã sản phẩm</a>' % up
    return ('<footer class="site-footer"><div class="footer-inner">'
            '<div class="footer-kicker">%(own)s · Cung cấp Endress+Hauser chính hãng tại Việt Nam</div>'
            '<div class="footer-main">'
            '<div class="footer-brand footer-column">'
            '<a class="footer-logo" href="%(up)s" aria-label="%(site)s"><img class="footer-logo-img" src="%(up)sassets/brand/eh-logo.png" alt="Endress+Hauser" width="61" height="34" />'
            '<span><span class="footer-logo-title">%(site)s</span><span class="footer-logo-sub">%(own)s</span></span></a>'
            '<p>Brand portal Endress+Hauser do %(own)s vận hành: tra mã thiết bị đo mức, áp suất, nhiệt độ và công tắc báo mức, '
            'đối chiếu datasheet, chọn cấu hình theo điều kiện quá trình và gửi RFQ cho nhà máy, EPC và đơn vị tích hợp hệ thống.</p>'
            '<div class="footer-company"><strong>Công ty TNHH Fast Group</strong><span>MST: %(mst)s</span>'
            '<span>fastgroup.vn/endress-hauser-viet-nam/</span></div></div>'
            '<div class="footer-column"><h3>Danh mục Endress+Hauser</h3><div class="footer-links">%(cats)s</div></div>'
            '<div class="footer-column"><h3>Hỗ trợ RFQ</h3><div class="footer-links">'
            '<a href="%(up)stim-kiem/">Tra mã Endress+Hauser</a><a href="%(up)slien-he/">Gửi BOM / RFQ</a>'
            '<a href="%(up)sblog/">Kiến thức đo lường</a><a href="%(up)sve-chung-toi/">Về Fast Group Engineering</a>'
            '<a href="%(root)sbrands/endress-hauser.html">Trang hãng trên fastgroup.vn</a></div></div>'
            '<div class="footer-column"><h3>Thông tin liên hệ</h3><div class="footer-contact">'
            '<div><span>Trụ sở</span><p>%(addr)s</p></div>'
            '<div><span>Vũng Tàu</span><p>%(addr2)s</p></div>'
            '<div><span>Điện thoại / Zalo</span><a href="tel:%(ph)s">%(pht)s</a></div>'
            '<div><span>Email</span><a href="mailto:%(mail)s">%(mail)s</a></div>'
            '</div></div></div>'
            '<div class="footer-cta"><div><strong>Cần báo giá Endress+Hauser chính hãng theo mã hoặc theo cấu hình?</strong>'
            '<span>Gửi mã model, điều kiện quá trình, kết nối và yêu cầu chứng nhận để nhận tư vấn cấu hình và báo giá.</span></div>'
            '<a class="button button-primary" href="%(up)slien-he/">Gửi RFQ Endress+Hauser</a></div>'
            '<div class="footer-bottom"><div>© 2026 <a href="%(root)s" target="_blank" rel="noopener">%(own)s</a>. All rights reserved.</div>'
            '<div>Website được vận hành độc lập nhằm hỗ trợ tra cứu, tư vấn và báo giá sản phẩm Endress+Hauser tại Việt Nam.</div>'
            '</div></div></footer>'
            '<script src="%(up)sassets/search-index.js"></script><script src="%(up)sassets/hero-search.js"></script>'
            '</body></html>') % dict(up=up, site=e(SITE), own=e(OWNER), mst=MST, cats=cats, root=ROOT,
                                     addr=e(ADDR), addr2=e(ADDR2), ph=PHONE, pht=PHONE_TXT, mail=EMAIL)

def breadcrumb_bar(up, trail):
    """trail: [(href_or_None, label)] ; muc cuoi href=None."""
    parts = []
    for href, label in trail:
        parts.append('<a href="%s%s">%s</a>' % (up, href, e(label)) if href is not None else '<span>%s</span>' % e(label))
    return '<nav class="breadcrumb-bar"><div class="container">%s</div></nav>' % ' › '.join(parts)

def bc_ld(items):
    return {"@context":"https://schema.org","@type":"BreadcrumbList",
            "itemListElement":[{"@type":"ListItem","position":i+1,"name":n,"item":u} for i,(n,u) in enumerate(items)]}

def faq_ld(pairs):
    return {"@context":"https://schema.org","@type":"FAQPage",
            "mainEntity":[{"@type":"Question","name":q,
                           "acceptedAnswer":{"@type":"Answer","text":a}} for q,a in pairs]}

def faq_html(pairs):
    return '<div class="faq-list">%s</div>' % ''.join(
        '<details class="faq-item"><summary>%s</summary><p>%s</p></details>' % (e(q), e(a)) for q, a in pairs)

def write(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
