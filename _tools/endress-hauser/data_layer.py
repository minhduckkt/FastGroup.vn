# -*- coding: utf-8 -*-
"""Nap va chuan hoa toan bo du lieu dau vao cho bo sinh site."""
import json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gen_lib as g
from taxonomy import MAIN, TECH, CAT2MAIN

HERE    = os.path.dirname(os.path.abspath(__file__))          # fastgroup.vn/_tools/endress-hauser
REPO    = os.path.abspath(os.path.join(HERE, '..', '..'))     # fastgroup.vn
OUT     = os.path.join(REPO, 'endress-hauser-viet-nam')       # thu muc site duoc publish
DATA    = os.path.join(HERE, 'data')
HUBSRC  = os.path.join(HERE, 'content', 'hubs')
BLOGSRC = os.path.join(HERE, 'content', 'blog')

CATALOG_VI = {'Level':'Đo mức liên tục','Pressure':'Đo áp suất','Point Level':'Công tắc báo mức','Temperature':'Đo nhiệt độ'}

def load():
    prods = json.load(open(os.path.join(DATA,'products_clean.json'), encoding='utf-8'))
    imgs  = json.load(open(os.path.join(DATA,'image_files.json'), encoding='utf-8'))
    plan  = json.load(open(os.path.join(DATA,'blog_plan.json'), encoding='utf-8'))

    # --- hub objects -----------------------------------------------------
    hubs = []
    for m in MAIN:
        meta, body = g.front_matter(open(os.path.join(HUBSRC, m['slug']+'.md'), encoding='utf-8').read())
        hubs.append(dict(m, kind='main', nav_label=m['nav'], meta=meta, body=body, items=[]))
    for t in TECH:
        meta, body = g.front_matter(open(os.path.join(HUBSRC, t['slug']+'.md'), encoding='utf-8').read())
        hubs.append(dict(t, kind='tech', nav_label=t['name'], meta=meta, body=body, items=[]))
    byslug = {h['slug']: h for h in hubs}
    tech_idx = {}
    for t in TECH:
        for pair in t['match']:
            tech_idx[pair] = t['slug']

    # --- products --------------------------------------------------------
    for p in prods:
        sku = p['sku'].strip()
        p['sku'] = sku
        p['slug'] = 'eh-' + g.slugify(sku)
        p['url']  = 'san-pham/%s/' % p['slug']
        p['abs']  = g.BASE + p['url']
        p['img']  = imgs[sku]
        p['main'] = CAT2MAIN[p['catalog']]
        p['tech'] = tech_idx.get((p['catalog'], p['category']))
        p['tone'] = byslug[p['tech']]['tone'] if p['tech'] else byslug[p['main']]['tone']
        p['catalog_vi'] = CATALOG_VI[p['catalog']]
        p['title'] = ('%s %s' % (p['family'], sku)) if p['family'] and p['family'].lower() not in sku.lower() else sku
        p['title'] = p['title'].strip()
        byslug[p['main']]['items'].append(p)
        if p['tech']:
            byslug[p['tech']]['items'].append(p)

    # --- blog ------------------------------------------------------------
    posts = []
    for row in plan:
        raw = open(os.path.join(BLOGSRC, row['slug'] + '.md'), encoding='utf-8').read()
        meta, body = g.front_matter(raw)
        body = re.sub(r'^#\s+.*\n', '', body, count=1).strip()   # bo H1 trung
        posts.append(dict(slug=row['slug'], model=row['model'], meta=meta, body=body,
                          links=[x.strip() for x in row['links'].split(';') if x.strip()],
                          nganh=row['nganh'],
                          kw=(meta.get('primary_keyword') or row.get('kw', '')).strip()))

    # --- gan bai viet vao san pham ---------------------------------------
    def norm(s): return re.sub(r'[^A-Z0-9]', '', str(s).upper())
    pidx = {}
    for p in prods:
        pidx.setdefault(norm(p['sku']), p)
        for part in re.split(r'[/+]', p['sku']):
            pidx.setdefault(norm(part), p)
    for post in posts:
        hit = None
        for cand in re.split(r'[/+]', post['model']) + [post['model']]:
            k = norm(cand)
            if k in pidx:
                hit = pidx[k]; break
        post['product'] = hit
        if hit is not None:
            hit.setdefault('posts', []).append(post)
    # lien ket nguoc: post['related_products'] tu cot "Lien ket noi bo"
    for post in posts:
        rel = []
        for token in post['links']:
            k = norm(token)
            if k in pidx and pidx[k] not in rel:
                rel.append(pidx[k])
        post['rel_products'] = rel[:4]

    for h in hubs:
        h['items'].sort(key=lambda x: (x['category'], x['sku']))
    return prods, hubs, byslug, posts
