# -*- coding: utf-8 -*-
"""Kiem tra site: link gay, anh thieu, JSON-LD, title/meta/canonical, trung lap."""
import os, re, sys, json, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from data_layer import OUT
import gen_lib as g

err = collections.defaultdict(list)
pages = []
for root, dirs, files in os.walk(OUT):
    for f in files:
        if f.endswith('.html'):
            pages.append(os.path.join(root, f))
pages.sort()

titles, canons, descs = {}, {}, {}
RX_A   = re.compile(r'(?:href|src)="([^"#][^"]*)"')
RX_T   = re.compile(r'<title>(.*?)</title>', re.S)
RX_C   = re.compile(r'<link rel="canonical" href="([^"]+)"')
RX_D   = re.compile(r'<meta name="description" content="([^"]*)"')
RX_LD  = re.compile(r'<script type="application/ld\+json">(.*?)</script>', re.S)
RX_H1  = re.compile(r'<h1[^>]*>(.*?)</h1>', re.S)

n_ld = 0
for path in pages:
    rel = os.path.relpath(path, OUT)
    html = open(path, encoding='utf-8').read()

    t = RX_T.search(html)
    if not t or not t.group(1).strip():
        err['thieu title'].append(rel)
    else:
        titles.setdefault(t.group(1), []).append(rel)
    d = RX_D.search(html)
    if not d or not d.group(1).strip():
        err['thieu meta description'].append(rel)
    else:
        descs.setdefault(d.group(1), []).append(rel)
        if len(d.group(1)) > 320:
            err['meta description qua dai (>320)'].append(rel)
    c = RX_C.search(html)
    if not c:
        err['thieu canonical'].append(rel)
    else:
        canons.setdefault(c.group(1), []).append(rel)
    h1 = RX_H1.findall(html)
    if len(h1) != 1:
        err['so luong H1 != 1'].append('%s (%d)' % (rel, len(h1)))

    for blob in RX_LD.findall(html):
        n_ld += 1
        try:
            json.loads(blob)
        except Exception as ex:
            err['JSON-LD loi'].append('%s: %s' % (rel, ex))

    for u in re.findall(r"url\('/endress-hauser-viet-nam/([^']+)'\)", html):
        if not os.path.exists(os.path.join(OUT, u)):
            err['anh hero (duong dan tuyet doi) khong ton tai'].append('%s -> %s' % (rel, u))

    base = os.path.dirname(path)
    for href in RX_A.findall(html):
        if href.startswith(('http', 'mailto:', 'tel:', 'data:', '//')):
            continue
        clean = href.split('?')[0].split('#')[0]
        if not clean:
            continue
        tgt = os.path.normpath(os.path.join(base, clean))
        if clean.endswith('/') or (os.path.isdir(tgt) and not os.path.splitext(clean)[1]):
            tgt = os.path.join(tgt, 'index.html')
        if not os.path.exists(tgt):
            err['link/anh gay'].append('%s -> %s' % (rel, href))

for k, v in titles.items():
    if len(v) > 1:
        err['title trung'].append('%s : %s' % (k[:60], v))
for k, v in canons.items():
    if len(v) > 1:
        err['canonical trung'].append('%s : %s' % (k, v))
for k, v in descs.items():
    if len(v) > 1:
        err['meta description trung'].append('%s... : %s' % (k[:60], v))

# anh mo coi
used = set()
for path in pages:
    html = open(path, encoding='utf-8').read()
    for m in re.findall(r'src="[^"]*assets/products/([^"]+)"', html):
        used.add(m)
have = set(os.listdir(os.path.join(OUT, 'assets', 'products')))
orphan = have - used
if orphan:
    err['anh khong duoc dung'].append('%d file' % len(orphan))

print('=' * 62)
print('KIEM TRA SITE ENDRESS+HAUSER VIET NAM')
print('=' * 62)
print('Trang HTML kiem tra : %d' % len(pages))
print('Khoi JSON-LD        : %d' % n_ld)
print('Title duy nhat      : %d' % len(titles))
print('Canonical duy nhat  : %d' % len(canons))
print('-' * 62)
total = 0
for k in sorted(err):
    v = err[k]
    total += len(v)
    print('[%3d] %s' % (len(v), k))
    for x in v[:8]:
        print('       - %s' % x)
    if len(v) > 8:
        print('       ... va %d muc nua' % (len(v) - 8))
if not total:
    print('KHONG CO LOI. Site san sang deploy.')
else:
    print('-' * 62)
    print('TONG SO VAN DE: %d' % total)
