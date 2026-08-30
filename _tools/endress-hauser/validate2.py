# -*- coding: utf-8 -*-
"""Kiem tra bo sung truoc khi commit: sitemap, search-index, placeholder sot, the bat buoc."""
import os, re, sys, json, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from data_layer import OUT
import gen_lib as g

err = collections.defaultdict(list)
BASE = g.BASE

def rel_of(url):
    assert url.startswith(BASE), url
    return url[len(BASE):]

def path_of(url):
    r = rel_of(url)
    return os.path.join(OUT, r, 'index.html') if (r == '' or r.endswith('/')) else os.path.join(OUT, r)

# --- 1. sitemap <-> filesystem ---------------------------------------
sm_urls = []
for f in ('sitemap-pages.xml', 'sitemap-products.xml', 'sitemap-blog.xml'):
    p = os.path.join(OUT, f)
    if not os.path.exists(p):
        err['sitemap thieu file'].append(f); continue
    sm_urls += re.findall(r'<loc>([^<]+)</loc>', open(p, encoding='utf-8').read())
for u in sm_urls:
    if not os.path.exists(path_of(u)):
        err['URL trong sitemap khong co file'].append(u)

html_pages = []
for root, d, fs in os.walk(OUT):
    for f in fs:
        if f.endswith('.html'):
            html_pages.append(os.path.join(root, f))
canon_set = set()
for p in html_pages:
    m = re.search(r'<link rel="canonical" href="([^"]+)"', open(p, encoding='utf-8').read())
    if m: canon_set.add(m.group(1))
missing_in_sitemap = canon_set - set(sm_urls)
if missing_in_sitemap:
    err['trang co canonical nhung khong nam trong sitemap'] += sorted(missing_in_sitemap)
extra = set(sm_urls) - canon_set
if extra:
    err['URL trong sitemap nhung khong khop canonical trang nao'] += sorted(extra)

idx_x = open(os.path.join(OUT, 'sitemap_index.xml'), encoding='utf-8').read()
for f in ('sitemap-pages.xml', 'sitemap-products.xml', 'sitemap-blog.xml'):
    if f not in idx_x:
        err['sitemap_index thieu tham chieu'].append(f)

# --- 2. search-index.js -----------------------------------------------
js = open(os.path.join(OUT, 'assets', 'search-index.js'), encoding='utf-8').read()
data = json.loads(js[js.index('=') + 1:].rstrip().rstrip(';'))
for row in data:
    u = row['url']            # dang '../san-pham/xxx/' — tinh tu /tim-kiem/
    tgt = os.path.normpath(os.path.join(OUT, 'tim-kiem', u))
    if not os.path.exists(os.path.join(tgt, 'index.html')):
        err['URL trong cong cu tra ma khong ton tai'].append(row['code'] + ' -> ' + u)
    for k in ('code', 'title', 'url'):
        if not str(row.get(k, '')).strip():
            err['muc tra ma thieu truong'].append(str(row)[:80])

# --- 3. quet loi soan thao / placeholder -----------------------------
BAD = [(r'assets/assets', 'duong dan anh bi nhan doi'),
       (r'%\(?[sd]\)?(?![0-9A-Za-z])(?![^<]*</script>)', 'con placeholder %s/%d chua thay'),
       (r'\bNone\b', 'lot chuoi None'),
       (r'&amp;amp;', 'escape HTML hai lan'),
       (r'\{\{', 'con dau ngoac template'),
       (r'\bnan\b|\bNaN\b', 'gia tri NaN')]
for p in html_pages:
    rel = os.path.relpath(p, OUT)
    body = open(p, encoding='utf-8').read()
    for rx, label in BAD:
        if re.search(rx, body):
            err[label].append(rel)

# --- 4. the bat buoc ---------------------------------------------------
for p in html_pages:
    rel = os.path.relpath(p, OUT)
    body = open(p, encoding='utf-8').read()
    for need, label in [('<html lang="vi">', 'thieu lang="vi"'),
                        ('name="viewport"', 'thieu the viewport'),
                        ('<meta charset="utf-8"', 'thieu charset'),
                        ('assets/site.css', 'khong nap site.css'),
                        ('og:image', 'thieu og:image'),
                        ('class="site-header"', 'thieu header'),
                        ('class="site-footer"', 'thieu footer')]:
        if need not in body:
            err[label].append(rel)
    if body.count('<main>') != 1 or body.count('</main>') != 1:
        err['the <main> khong dung 1 cap'].append(rel)
    if not body.rstrip().endswith('</html>'):
        err['file khong ket thuc bang </html>'].append(rel)

# --- 5. robots ---------------------------------------------------------
rb = open(os.path.join(OUT, 'robots.txt'), encoding='utf-8').read()
if BASE + 'sitemap_index.xml' not in rb:
    err['robots.txt cua portal sai sitemap'].append(rb.strip()[:80])

# --- 6. JSON-LD: kieu schema tren tung loai trang ----------------------
need_type = {'san-pham/': ['Product', 'BreadcrumbList', 'FAQPage'],
             'blog/': ['Article', 'BreadcrumbList']}
for p in html_pages:
    rel = os.path.relpath(p, OUT).replace('\\', '/')
    if rel in ('blog/index.html',): continue
    body = open(p, encoding='utf-8').read()
    types = set()
    for blob in re.findall(r'<script type="application/ld\+json">(.*?)</script>', body, re.S):
        try: types.add(json.loads(blob).get('@type'))
        except Exception: pass
    for pref, req in need_type.items():
        if rel.startswith(pref) and rel != pref + 'index.html':
            for t in req:
                if t not in types:
                    err['trang thieu schema ' + t].append(rel)

print('=' * 64)
print('KIEM TRA BO SUNG TRUOC KHI COMMIT')
print('=' * 64)
print('Trang HTML          : %d' % len(html_pages))
print('URL trong sitemap   : %d' % len(sm_urls))
print('Muc trong tra ma    : %d' % len(data))
print('-' * 64)
tot = 0
for k in sorted(err):
    v = err[k]; tot += len(v)
    print('[%3d] %s' % (len(v), k))
    for x in v[:6]: print('       - %s' % x)
    if len(v) > 6: print('       ... va %d muc nua' % (len(v) - 6))
print('-' * 64)
print('KHONG CO VAN DE.' if not tot else 'TONG SO VAN DE: %d' % tot)
