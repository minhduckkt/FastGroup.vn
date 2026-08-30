# -*- coding: utf-8 -*-
"""Sinh toan bo mini-site Endress+Hauser Viet Nam."""
import sys, os, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from data_layer import load, OUT
import gen_pages as P

t0 = time.time()
prods, hubs, byslug, posts = load()
P.build_home(hubs, byslug, prods, posts)
P.build_products_index(hubs, byslug, prods)
for h in hubs:
    P.build_hub(h, hubs, byslug, posts)
for p in prods:
    P.build_product(p, hubs, byslug, prods)
P.build_blog_index(hubs, byslug, posts)
for ps in posts:
    P.build_post(ps, hubs, byslug, posts)
P.build_search(hubs, byslug, prods)
P.build_contact(hubs)
P.build_about(hubs)
n_idx = P.build_search_index(prods, hubs, posts)
n_url = P.build_sitemaps(prods, hubs, posts)
n_html = sum(1 for r, d, fs in os.walk(OUT) for f in fs if f.endswith('.html'))
print('trang HTML :', n_html)
print('san pham   :', len(prods))
print('hub        :', len(hubs))
print('bai blog   :', len(posts))
print('search idx :', n_idx, 'muc')
print('sitemap    :', n_url, 'URL')
print('thoi gian  : %.1fs' % (time.time() - t0))
