# -*- coding: utf-8 -*-
"""Buoc 2: tao ban anh nen trong suot trong assets/hero/ de dung lam background hero.

Anh catalog co nen trang/xam nhat. Neu dat thang lam background hero se thanh mot o
chu nhat sang giua nen gradient toi. Script nay flood-fill tu vien de tach nen,
lam mem bien roi ghi ra assets/hero/ cung ten file.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from data_layer import OUT
from PIL import Image, ImageDraw, ImageFilter
import numpy as np

SENTINEL = (255, 0, 255)
THRESH   = 34        # nguong mau khi flood-fill tu vien
MIN_FRAC = 0.05      # neu tach duoc < 5% dien tich thi coi nhu that bai, giu anh goc


def main():
    src = os.path.join(OUT, 'assets', 'products')
    dst = os.path.join(OUT, 'assets', 'hero')
    os.makedirs(dst, exist_ok=True)
    n = kept = 0
    for f in sorted(os.listdir(src)):
        if not f.lower().endswith('.png'):
            continue
        im = Image.open(os.path.join(src, f)).convert('RGB')
        im.thumbnail((900, 900))
        w, h = im.size
        work = im.copy()
        seeds = [(0, 0), (w-1, 0), (0, h-1), (w-1, h-1), (w//2, 0), (w//2, h-1), (0, h//2), (w-1, h//2)]
        for xy in seeds:
            try:
                ImageDraw.floodfill(work, xy, SENTINEL, thresh=THRESH)
            except Exception:
                pass
        a = np.array(work)
        mask = (a[..., 0] == 255) & (a[..., 1] == 0) & (a[..., 2] == 255)
        if mask.mean() < MIN_FRAC:
            alpha = np.full((h, w), 255, np.uint8); kept += 1
        else:
            alpha = np.where(mask, 0, 255).astype(np.uint8)
        am = Image.fromarray(alpha).filter(ImageFilter.GaussianBlur(0.6))
        out = im.convert('RGBA'); out.putalpha(am)
        out.save(os.path.join(dst, f), optimize=True)
        n += 1
    print('Da tao %d anh hero (%d anh khong tach duoc nen, giu nguyen).' % (n, kept))


if __name__ == '__main__':
    main()
