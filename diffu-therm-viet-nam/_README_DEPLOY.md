# Diffu-Therm Việt Nam - Brand Portal SEO

**Vận hành:** Fast Group Engineering  
**Đường dẫn đề xuất:** `https://fastgroup.vn/diffu-therm-viet-nam/`  
**Build:** 2026-08-30  
**Nguồn dữ liệu:** `53. Diffu-therm/data/products.json`, `documents.json`, `images.json`, `source_pages.json`

## 1. Thống kê site

| Hạng mục | Số lượng |
|---|---:|
| Trang HTML mini-site | 47 |
| Trang sản phẩm | 29 |
| Trang danh mục kỹ thuật | 4 |
| Bài blog SEO nền | 8 |
| Ảnh sản phẩm copy vào site | 21 |
| Dòng tài liệu map theo sản phẩm | 129 |
| Sitemap riêng | 4 file |

## 2. Cấu trúc

```text
diffu-therm-viet-nam/
├── index.html
├── san-pham/
│   ├── index.html
│   └── diffu-therm-<ma-hang>/
├── kiem-tra-tham-thau-pt-diffu-therm/
├── kiem-tra-hat-tu-mt-diffu-therm/
├── he-thong-c-200c-diffu-therm/
├── he-thong-uv-huynh-quang-diffu-therm/
├── blog/
├── tim-kiem/
├── lien-he/
├── ve-chung-toi/
├── assets/
├── sitemap_index.xml
├── sitemap-pages.xml
├── sitemap-products.xml
├── sitemap-blog.xml
└── robots.txt
```

## 3. SEO đã triển khai

- **Brand intent:** `Diffu-Therm Việt Nam`, `Diffu-Therm chính hãng Đức`, `nhà phân phối chính hãng Diffu-Therm`.
- **Visual identity:** tím đậm + đen là màu chủ đạo cho cảm giác UV/NDT/khoa học; tím sáng dùng cho UV fluorescence, đen/than dùng cho MT, cam chỉ giữ làm màu phụ cho System C 200°C.
- **NDT intent:** `vật tư kiểm tra không phá hủy NDT`, `liquid penetrant testing`, `magnetic particle testing`, `UV fluorescent penetrant testing`.
- **Method hubs:** PT, MT, UV huỳnh quang, System C đến 200°C.
- **Part-number targeting:** mỗi mã có URL riêng `/san-pham/diffu-therm-<ma>/`.
- **Schema.org:** Organization, WebSite SearchAction, BreadcrumbList, ItemList, Product, FAQPage, Article.
- **Internal linking:** home -> category -> product -> related product; blog -> money page/category/product.
- **RFQ B2B:** không công bố giá khi chưa có price list chính thức; chuyển đổi bằng CTA gửi RFQ, SDS/manual, CO/CQ.
- **Sitemap:** thêm sitemap riêng vào `fastgroup.vn/robots.txt`; thêm brand page và mini-site home vào root `sitemap.xml`.

## 4. Công cụ build và kiểm tra

```powershell
node ".\53. Diffu-therm\tools\generate_diffutherm_site.mjs"
node ".\53. Diffu-therm\tools\validate_diffutherm_site.mjs"
```

Kết quả validation hiện tại: 49 trang kiểm tra, 0 link/ảnh thiếu, 0 JSON-LD lỗi, 0 trang thiếu title/meta/canonical.

## 5. Việc nên làm sau publish

- Submit `https://fastgroup.vn/diffu-therm-viet-nam/sitemap_index.xml` vào Google Search Console.
- Index thủ công 5 URL trọng điểm: home, PT category, MT category, `BDR-L`, `MPS-F`.
- Khi có price list chính thức, thêm vào quy trình RFQ nội bộ; không public giá nếu giá biến động theo lô/lead time.
- Nếu có logo Diffu-Therm chính thức được phép dùng, thay ảnh đại diện hiện tại trong `img/diffu-therm-ndt-product.png`.
