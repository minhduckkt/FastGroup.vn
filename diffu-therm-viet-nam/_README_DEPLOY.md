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

---

## Sửa lỗi 2026-08-30 (quan trọng — đọc trước khi build lại)

Ba lỗi hiển thị đã được sửa **trên output**. Bộ sinh (`generate_*.mjs`) nằm ngoài repo và **chưa được sửa**,
nên nếu build lại mà không vá script thì cả ba lỗi sẽ quay lại.

### 1. Ảnh hero không hiển thị — đường dẫn bị nhân đôi

`--hero-image` / `--page-image` đặt inline trong thẻ `style` của HTML, nhưng trình duyệt phân giải URL tương đối
trong biến CSS **theo vị trí file stylesheet** (`assets/site.css`), không theo vị trí trang. Hệ quả:

| Độ sâu trang | Đường dẫn cũ | Trình duyệt hiểu thành | Kết quả |
|---|---|---|---|
| Trang chủ | `url('assets/x.png')` | `assets/assets/x.png` | ✗ mất ảnh |
| Trang danh mục | `url('../assets/x.png')` | `assets/x.png` | ✓ đúng (tình cờ) |
| Trang sản phẩm / blog | `url('../../assets/x.png')` | trên cả thư mục gốc | ✗ mất ảnh |

**Cách sửa trong bộ sinh:** luôn xuất đường dẫn tuyệt đối theo gốc site, ví dụ
`--hero-image:url('/wika-viet-nam/assets/images/hero/hero-gauge.webp')`.
Đã sửa thủ công: WIKA 52 trang, Diffu-Therm 23 trang.

### 2. `.check-list` vỡ mỗi từ một dòng

`.check-list li{display:grid;grid-template-columns:28px 1fr}` — khi `<li>` chứa `<strong>` rồi mới tới phần text,
phần text trở thành ô lưới thứ 3 và bị đẩy xuống cột rộng 28px. Đã override thành `display:block` +
`::before` định vị tuyệt đối (ghi ở cuối `assets/site.css`).

### 3. `.lead` chữ trắng trên nền sáng

`.lead` trong CSS nền được định nghĩa màu trắng (dành cho hero tối), nhưng cũng được dùng trong `.product-hero`
vốn có nền sáng → chữ gần như vô hình. Đã override `.product-hero .lead{color:var(--muted)}`.

Ba bản vá CSS nằm ở cuối `assets/site.css`, đánh dấu bằng comment `fix 2026-08-30`.
