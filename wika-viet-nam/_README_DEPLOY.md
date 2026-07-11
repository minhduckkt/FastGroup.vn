# WIKA Việt Nam — Website (Folder 4) · Sẵn sàng deploy

**Vận hành:** Fast Group Engineering · Deploy dưới `https://fastgroup.vn/wika-viet-nam/`
**Build:** 2026-07-10 · Nguồn dữ liệu: `products_master.json` (301 model WIKA chính hãng)

## 1. Thống kê site

| Hạng mục | Số lượng |
|---|---|
| Trang HTML | 371 |
| Trang sản phẩm (`/san-pham/<slug>/`) | 301 + 18 redirect |
| Trang danh mục (11 nhóm gốc WIKA) | 11 |
| Bài blog SEO | 34 |
| Ảnh sản phẩm | 373 |
| Khối JSON-LD (schema) | 1.313 — 100% hợp lệ |
| Link gãy / ảnh thiếu | 0 |
| Dung lượng | ~26 MB |

## 2. Cấu trúc

```
4. Wika website mới_claude.ai/
├── index.html                → Trang chủ
├── do-ap-suat-wika/          → 11 category hub (do-nhiet-do-wika, do-muc-wika, do-luu-luong-wika,
│                                do-luc-wika, hieu-chuan-wika, khi-sf6-wika, hydro-wika, iiot-wika,
│                                ung-dung-cong-nghiep-wika, san-pham-wika-khac)
├── san-pham/
│   ├── index.html            → Danh mục tất cả 301 sản phẩm
│   └── wika-<order-code>/     → 301 trang sản phẩm
├── tra-ma-wika/              → Cross-reference / tra part number
├── blog/                     → 34 bài blog (giữ nguyên từ template)
├── ve-chung-toi/  lien-he/  tim-kiem/
├── assets/  (site.css, hero-search.js, search-index.js, images/, products/)
├── sitemap_index.xml → sitemap-products.xml (301) + sitemap-pages.xml (17) + sitemap-blog.xml
└── robots.txt
```

## 3. SEO đã triển khai

- **Order-code targeting:** mỗi mã hàng có 1 URL riêng `/san-pham/wika-<mã>/` → bắt truy vấn "wika + mã".
- **Schema.org:** Product + Offer + BreadcrumbList + FAQPage + Organization + WebSite (SearchAction).
- **Từ khóa chủ đích** phủ trên trang chủ, H1/H2, meta, alt ảnh, footer: *WIKA Việt Nam, WIKA chính hãng Đức, nhà cung cấp WIKA chính hãng, Fast Group Engineering, mua WIKA chính hãng ở đâu*.
- **Meta động** theo model + category cho 301 trang.
- **Internal linking:** product ↔ category ↔ related products; blog làm supporting content.
- **Sitemap + canonical tuyệt đối**; 18 slug cũ chuyển thành redirect `noindex` → sản phẩm thật (tránh duplicate content).
- **Tính năng thông minh:** autocomplete theo order code (hero + trang Tìm kiếm), datasheet trỏ tài liệu WIKA chính hãng, form RFQ gắn theo từng model (`lien-he/?model=...`).
- **Chính sách giá:** ẩn giá EUR công khai, thay bằng CTA "Yêu cầu báo giá" (chuẩn B2B lead-gen).

## 4. Deploy (GitHub Pages)

1. Copy toàn bộ nội dung Folder 4 vào repo, đặt dưới thư mục `wika-viet-nam/`.
2. Bật GitHub Pages (branch `main`, root hoặc `/docs`).
3. Đảm bảo site phục vụ tại path `/wika-viet-nam/` (khớp canonical & redirect tuyệt đối).
4. Submit `sitemap_index.xml` vào Google Search Console.

## 5. Cần rà trước khi publish (khuyến nghị)

- [ ] Kiểm tra vài trang sản phẩm trên trình duyệt thật (layout, ảnh).
- [ ] Xác nhận MST trong footer (đang để `0315555189` từ template).
- [ ] Cân nhắc bổ sung ảnh cho 2 model chưa có ảnh.
- [ ] Rich Results Test (Google) cho 1 trang Product + 1 trang FAQ.
