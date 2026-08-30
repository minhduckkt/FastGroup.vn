# Endress+Hauser Việt Nam — Brand Portal SEO

**Vận hành:** Fast Group Engineering
**Đường dẫn deploy:** `https://fastgroup.vn/endress-hauser-viet-nam/`
**Build:** 2026-08-30
**Nguồn dữ liệu:** `eh-portal/data/products.csv` (171 dòng → 160 SKU sau khi gộp trùng),
`blog-endress-hauser/*.md` (41 bài), `EH_Blog_Content_Plan.xlsx`, kho ảnh `eh-portal/images` + `images/` + `images_level/`.

## 1. Thống kê site

| Hạng mục | Số lượng |
|---|---:|
| Trang HTML | 221 |
| Trang sản phẩm `/san-pham/eh-<mã>/` | 160 |
| Hub danh mục (4 lĩnh vực + 10 công nghệ) | 14 |
| Bài blog | 41 |
| Trang phụ (home, san-pham, blog index, tra mã, liên hệ, về chúng tôi) | 6 |
| Ảnh sản phẩm | 160 (+160 bản nền trong suốt cho hero) |
| Khối JSON-LD | 836 — 100% hợp lệ |
| Link gãy / ảnh thiếu | 0 |
| Title / canonical trùng | 0 |
| Mục trong công cụ tra mã | 215 |

## 2. Cấu trúc

```text
endress-hauser-viet-nam/
├── index.html
├── do-muc-endress-hauser/               ← 4 hub lĩnh vực
├── do-ap-suat-endress-hauser/
├── cong-tac-muc-endress-hauser/
├── do-nhiet-do-endress-hauser/
├── radar-do-muc-micropilot/             ← 10 hub công nghệ
├── radar-dan-song-levelflex/
├── sieu-am-do-muc-prosonic/
├── do-muc-thuy-tinh-deltapilot-waterpilot/
├── cam-bien-ap-suat-cerabar-ceraphant/
├── cam-bien-chenh-ap-deltabar/
├── cong-tac-muc-rung-liquiphant-soliphant/
├── cong-tac-muc-dien-dung-dan-dien/
├── bo-chuyen-doi-tin-hieu-nhiet-itemp/
├── nhiet-ke-cong-nghiep-itherm-omnigrad/
├── san-pham/
│   ├── index.html
│   └── eh-<mã>/                          ← 160 trang model
├── blog/  (index + 41 bài)
├── tim-kiem/  lien-he/  ve-chung-toi/
├── assets/  (site.css, hero-search.js, search-index.js, products/, hero/)
├── sitemap_index.xml → sitemap-pages.xml + sitemap-products.xml + sitemap-blog.xml
└── robots.txt
```

## 3. SEO đã triển khai

- **Model targeting:** mỗi mã có URL riêng `/san-pham/eh-<mã>/` → bắt truy vấn "Endress Hauser + mã".
- **Hai tầng danh mục:** 4 hub lĩnh vực (từ khóa rộng: *thiết bị đo mức Endress+Hauser*) + 10 hub công nghệ
  (từ khóa dài: *radar đo mức Micropilot*, *công tắc mức Liquiphant*, *bộ chuyển đổi nhiệt iTEMP*…).
  Mỗi hub là một bài kỹ thuật 950–1.550 từ, không phải trang danh sách rỗng.
- **Schema.org:** Organization, WebSite (SearchAction), Product + Offer, BreadcrumbList, ItemList, FAQPage, Article, Blog, ContactPage.
- **Internal linking:** home → hub lĩnh vực → hub công nghệ → trang model → model liên quan;
  blog → trang model + hub + model nên so sánh (lấy từ cột "Liên kết nội bộ" của `EH_Blog_Content_Plan.xlsx`).
- **Meta động** theo model, hub và bài viết; 221/221 title và canonical duy nhất.
- **Tra mã:** autocomplete ở hero + trang `/tim-kiem/`, index 215 mục (model, hub, bài viết), không cần backend.
- **RFQ theo model:** nút trên trang model dẫn tới `lien-he/?model=<mã>` và tự điền vào biểu mẫu.
- **Chính sách giá:** không công bố giá, chuyển đổi bằng RFQ — đúng chuẩn B2B và tránh đăng giá không có nguồn.
- **Caveat dữ liệu:** mọi trang model đều nhắc đối chiếu Technical Information (TI) đúng mã đặt hàng trên endress.com.

## 4. Tích hợp vào site mẹ (đã làm)

- `fastgroup.vn/robots.txt` — thêm `Sitemap: https://fastgroup.vn/endress-hauser-viet-nam/sitemap_index.xml`.
- `fastgroup.vn/sitemap.xml` — thêm home portal, `/san-pham/`, `/blog/`.
- `fastgroup.vn/brands/endress-hauser.html` — thêm link "Tra cứu thêm catalog", nút "Mở brand portal",
  khối "Tra cứu 160 model Endress+Hauser" liệt kê 12 hub, và nút RFQ trong cta-band (17 link tới portal).

## 5. Công cụ build và kiểm tra

```powershell
python "eh-build\build.py"        # sinh lại toàn bộ 221 trang (~2.5s)
python "eh-build\validate.py"     # kiểm tra link, ảnh, JSON-LD, title/meta/canonical
```

Nguồn của bộ sinh nằm trong `eh-build/`:
`taxonomy.py` (14 hub), `hubs/*.md` (nội dung hub), `gen_lib.py` (markdown + template),
`data_layer.py` (nạp dữ liệu), `render_parts.py` (khối HTML), `gen_pages.py` (sinh trang).

Kết quả validate hiện tại: **221 trang, 836 khối JSON-LD, 0 lỗi.**

## 6. Việc nên làm sau khi publish

- Submit `https://fastgroup.vn/endress-hauser-viet-nam/sitemap_index.xml` vào Google Search Console.
- Index thủ công 6 URL trọng điểm: home, `do-muc-endress-hauser`, `radar-do-muc-micropilot`,
  `san-pham/eh-fmr20b-fmr30b`, `san-pham/eh-pmp71b`, `san-pham/eh-ftl51`.
- Rich Results Test cho 1 trang Product và 1 trang FAQ.
- Cân nhắc bổ sung bài blog cho các model chưa có bài (hiện 41/160 model có bài phân tích riêng).
- Khi có logo Endress+Hauser được phép dùng, thay ô chữ "E+H" trong header/footer bằng logo thật
  (sửa hàm `header()` / `footer()` trong `eh-build/gen_lib.py` rồi build lại).
