# -*- coding: utf-8 -*-
"""Buoc 1 cua pipeline: tu products.csv goc -> products_clean.json + copy anh san pham.

Chay lai buoc nay khi products_master.csv thay doi hoac khi bo sung anh moi.
Kho anh goc nam NGOAI repo (qua lon de version); dua duong dan qua --src.

    python prepare_data.py --src "D:\\...\\9. Loc du lieu cho Endress and Hauser"
"""
import argparse, csv, collections, json, os, re, shutil, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from data_layer import HERE, DATA, OUT
import gen_lib as g

IMG_DIRS = ['eh-portal/images', 'images_level', 'images']   # tuong doi so voi --src


def dedupe(csv_path):
    rows = list(csv.DictReader(open(csv_path, encoding='utf-8-sig')))
    by = collections.OrderedDict()
    for r in rows:
        sku = r['sku'].strip()
        if sku in by:                       # gop dong trung: giu gia tri dai nhat moi cot
            for k, v in r.items():
                if len((v or '').strip()) > len((by[sku][k] or '').strip()):
                    by[sku][k] = v
        else:
            by[sku] = dict(r)
    merged = [k for k, v in collections.Counter(r['sku'].strip() for r in rows).items() if v > 1]
    return list(by.values()), rows, merged


def build_image_index(src):
    pool = {}
    for d in IMG_DIRS:
        full = os.path.join(src, d)
        if not os.path.isdir(full):
            continue
        for f in sorted(os.listdir(full)):
            if not f.lower().endswith(('.png', '.jpg', '.webp')) or f.startswith('HERO_'):
                continue
            stem = os.path.splitext(f)[0]
            key = stem.upper().replace('_HYD', '').replace('_SOL', '').replace('-SOL', '')
            pool.setdefault(key, os.path.join(full, f))
    norm = lambda s: re.sub(r'[^A-Z0-9+]', '', s.upper())
    alt = {}
    for key, path in pool.items():
        alt.setdefault(norm(key), path)
        parts = key.split('-')                 # FMB51-52-53 -> FMB51, FMB52, FMB53
        if len(parts) > 1:
            m = re.match(r'^([A-Z]+)', parts[0])
            pref = m.group(1) if m else ''
            for p in parts:
                cand = p if re.match(r'^[A-Z]{2,}', p) else pref + p
                alt.setdefault(norm(cand), path)
    return alt


def resolve_images(prods, alt):
    norm = lambda s: re.sub(r'[^A-Z0-9+]', '', s.upper())
    res, missing = {}, []
    for p in prods:
        sku = p['sku'].strip()
        cands = [sku] + [x.strip() for x in re.split(r'[/+]', sku)] + [re.sub(r'\(.*?\)', '', sku).strip()]
        m = re.match(r'^([A-Z]+\d+[A-Z]*)', sku.upper())
        if m:
            cands.append(m.group(1))
        hit = next((alt[norm(c)] for c in cands if norm(c) in alt), None)
        if not hit:                             # du phong: cung ho san pham
            m2 = re.match(r'^([A-Z]{3})', norm(sku))
            if m2:
                hit = next((v for k, v in alt.items() if k.startswith(m2.group(1))), None)
        (res.setdefault(sku, hit) if hit else missing.append(sku))
    return res, missing


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--src', required=True, help='thu muc goc chua eh-portal/, images/, images_level/')
    a = ap.parse_args()

    prods, rows, merged = dedupe(os.path.join(DATA, 'products_master.csv'))
    print('CSV goc %d dong -> %d SKU (gop %d ma trung: %s)' % (len(rows), len(prods), len(merged), ', '.join(merged)))
    json.dump(prods, open(os.path.join(DATA, 'products_clean.json'), 'w', encoding='utf-8'),
              ensure_ascii=False, indent=1)

    alt = build_image_index(a.src)
    img_map, missing = resolve_images(prods, alt)
    if missing:
        print('CANH BAO: %d SKU khong tim duoc anh: %s' % (len(missing), missing))
    json.dump(img_map, open(os.path.join(DATA, 'image_map.json'), 'w', encoding='utf-8'),
              ensure_ascii=False, indent=1)

    dst = os.path.join(OUT, 'assets', 'products')
    os.makedirs(dst, exist_ok=True)
    files = {}
    for sku, srcpath in img_map.items():
        name = 'eh-' + g.slugify(sku) + os.path.splitext(srcpath)[1].lower()
        target = os.path.join(dst, name)
        if not os.path.exists(target):
            shutil.copy2(srcpath, target)
        files[sku] = name
    json.dump(files, open(os.path.join(DATA, 'image_files.json'), 'w', encoding='utf-8'),
              ensure_ascii=False, indent=1)
    print('Anh san pham: %d SKU -> %d file trong assets/products/' % (len(files), len(set(files.values()))))
    print('Xong. Chay tiep: python make_hero_images.py  roi  python build.py')


if __name__ == '__main__':
    main()
