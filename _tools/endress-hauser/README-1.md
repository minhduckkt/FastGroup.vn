# Bộ sinh site — Qlight Việt Nam

Sinh toàn bộ `fastgroup.vn/qlight-viet-nam/` (**4.222 trang**) từ ba nguồn dữ liệu.
**Không sửa tay file HTML đã sinh** — mọi thay đổi sẽ bị ghi đè ở lần build sau.

## Chạy nhanh

```powershell
cd "D:\20. Các website\Fastgroup.vn\Fast Group\_tools\qlight"
python prepare_data.py     # gộp 3 nguồn, copy ảnh — chỉ chạy khi nguồn đổi
python make_assets.py      # sinh site.css + hero-search.js — chạy khi CSS của E+H đổi
python make_hero_images.py # tách nền ảnh làm background hero (cần pillow + numpy)
python build.py            # sinh toàn bộ trang (~2,5 giây)
python validate.py         # link, ảnh, JSON-LD, title/canonical trùng
python validate2.py        # sitemap, tra mã, placeholder sót, độ phủ dữ liệu
```

Bước 1–3 chỉ cần chạy khi dữ liệu nguồn hoặc ảnh thay đổi. Ngày thường chỉ cần
`build.py` + hai lệnh validate.

## Ba nguồn dữ liệu

| Nguồn | Đường dẫn mặc định | Nội dung |
|---|---|---|
| Catalog qlight.com | `D:\101. Tài liệu kỹ thuật\6.QLIGHT\6. Du an download san pham cua Qlight\qlight_data` | 598 sản phẩm: features, spec tables, SEO, 1.608 ảnh |
| Part number qlight.vn | `D:\20. Các website\Qlight\Qlight` | `assets/data/part_numbers.csv` — 3.284 mã, 482 model |
| Taxonomy | `taxonomy.py` trong thư mục này | 8 danh mục gốc → 31 nhóm → 120 series |

Đổi đường dẫn bằng `--scrape` và `--qlightvn` khi chạy `prepare_data.py`.

## Năm tầng trang

| Tầng | Số trang | URL | Vai trò |
|---|---:|---|---|
| Danh mục gốc | 8 | `/<slug>/` | Bài dài, gánh cụm từ khóa chính |
| Nhóm sản phẩm | 31 | `/<slug>/` | Bài vừa, từ khóa nhóm |
| Series | 120 | `/<slug>/` | Bài ngắn + bảng model + bảng mã hàng |
| **Model** | **773** | `/model/<slug>/` | Features, bảng thông số hãng, ảnh, danh sách mã hàng |
| Mã hàng | 3.284 | `/san-pham/<slug>/` | Thông số giải mã + link về model |
| Trang phụ | 6 | | chủ, tra mã, tất cả sản phẩm, blog, liên hệ, về chúng tôi |

Slug của cả ba tầng hub đều duy nhất nên URL để phẳng, không lồng thư mục.

**Vì sao có tầng model:** 3.284 mã hàng của cùng một model chỉ khác điện áp/màu/kiểu lắp
nên nội dung gần trùng nhau — đúng lỗi khiến 93% trang của qlight.vn cũ không tạo ra
lượt hiển thị nào. Tầng model là nơi đặt nội dung thật (features + bảng thông số hãng +
ảnh), còn trang mã hàng giữ vai trò tra cứu và trỏ ngược về model.

Trong 773 model có **291 model chỉ có dữ liệu catalog** — có trên qlight.com nhưng
catalog tiếng Việt không tách thành part number. Vẫn sinh trang (đủ ảnh + thông số),
chỉ thay bảng mã hàng bằng lời mời gửi RFQ tra mã.

## Cấu trúc

```text
_tools/qlight/
├── taxonomy.py            → ★ 8 MAIN + 31 GROUPS + 120 SERIES (159 slug, đã khử trùng)
├── matching.py            → khớp data_model ↔ prodcode, 4 mức tin cậy
├── prepare_data.py        → bước 1: gộp dữ liệu, copy ảnh → data/*.json
├── make_assets.py         → sinh site.css (fork từ E+H, đổi màu) + hero-search.js
├── make_hero_images.py    → tách nền ảnh sản phẩm cho background hero
├── data_layer.py          → nạp data/*.json, gắn taxonomy, đọc content/
├── gen_lib.py             → ★ thông tin công ty, header/footer, markdown, JSON-LD
├── render_parts.py        → khối HTML dùng lại: bảng thông số, thẻ model, FAQ
├── gen_pages.py           → sinh từng loại trang
├── build.py               → điều phối
├── validate.py            → link, ảnh, JSON-LD, thẻ meta, trùng title/canonical
├── validate2.py           → sitemap, tra mã, placeholder, độ phủ dữ liệu
├── content/               → ★ nội dung biên tập (chưa có — bước C)
│   ├── mains/<slug>.md    →   8 bài 1.200–1.500 từ
│   ├── groups/<slug>.md   →  31 bài 600–900 từ
│   ├── series/<slug>.md   → 120 bài 400–700 từ
│   └── blog/<slug>.md     → bài kiến thức
└── data/                  → dẫn xuất từ prepare_data.py, có commit vào repo
    ├── products_clean.json   588 sản phẩm đã gắn series/nhóm/danh mục
    ├── models.json           773 model, mức khớp, danh sách mã hàng
    ├── parts.json          3.284 mã hàng đã gắn slug/URL/model
    ├── image_files.json      prodcode → tên file trong assets/products/
    └── match_report.json     báo cáo khớp để soát bằng mắt
```

★ = file nên sửa khi muốn thay đổi nội dung.

## Bốn mức khớp dữ liệu

`part_numbers.csv` dùng cột **`data_model`** (cột `model` bị hỏng: 58% số dòng chứa mô tả
tiếng Việt thay vì mã). Mỗi model được khớp với sản phẩm scrape theo bốn mức:

| Mức | Số mã | Được kế thừa |
|---|---:|---|
| `strong` | 3.031 | ảnh, features, bảng thông số hãng, SEO, vị trí taxonomy |
| `alias` | 103 | chỉ ảnh + vị trí taxonomy (bảng `ALIAS` trong `matching.py`) |
| `prefix` | 134 | chỉ ảnh + vị trí taxonomy (khớp theo tiền tố dài nhất) |
| `fallback` | 16 | chỉ vị trí taxonomy (bảng `SERIES_FALLBACK`) |
| `catalog` | — | sản phẩm gốc, kế thừa đầy đủ |

Lý do tách mức: gán bảng thông số của QTC50L cho MTC50L là sai sự thật kỹ thuật, nhưng
xếp MTC50L vào đúng series đèn tháp thì vẫn đúng. Mở `data/match_report.json` để soát.

Muốn sửa một khớp sai: thêm dòng vào `ALIAS` (trỏ sang prodcode tương đương) hoặc
`SERIES_FALLBACK` (trỏ thẳng sang series slug) trong `matching.py`, rồi chạy lại
`prepare_data.py`.

## Muốn sửa gì thì sửa ở đâu

| Muốn thay đổi | Sửa file |
|---|---|
| Nội dung một trang danh mục / nhóm / series | `content/{mains,groups,series}/<slug>.md` |
| Bài blog | `content/blog/<slug>.md` |
| Thêm/bớt nhóm, đổi cây danh mục | `taxonomy.py` |
| Khớp model sai | `matching.py` → chạy lại `prepare_data.py` |
| Thông tin công ty, email, địa chỉ, số giấy chứng nhận | phần đầu `gen_lib.py` |
| Màu sắc, giao diện | `make_assets.py` (biến màu) → chạy lại |
| Cấu trúc trang, JSON-LD | `gen_pages.py` |

### Front matter của file content

```yaml
---
meta_title: "Tiêu đề thẻ <title>"
meta_desc: "Meta description"
h1: "Tiêu đề H1 nếu khác tên danh mục"
eyebrow: "Chữ nhỏ phía trên H1"
lead: "Đoạn mở đầu trong hero"
---
```

Thiếu trường nào thì bộ sinh tự đặt theo dữ liệu, nên có thể viết dần từng danh mục.

## Quy ước bắt buộc giữ

- **Đường dẫn ảnh hero phải tuyệt đối**: `url('/qlight-viet-nam/assets/hero/x.png')`.
  Trình duyệt phân giải URL tương đối trong biến CSS theo vị trí *file CSS*, không theo trang.
- **Nút RFQ dùng fragment** `lien-he/#model=<mã>`, **không** dùng `?model=`.
  Chính pattern query đã tạo 1.017 URL rác trên qlight.vn cũ; với 3.284 trang sẽ thành 3.284 URL rác.
  `validate2.py` có kiểm tra riêng cho lỗi này.
- **Không công bố giá.** Chuyển đổi bằng RFQ.
- **Trường trống thì để trống**, không suy đoán cho đầy bảng thông số.
- **Logo Qlight dùng với tư cách nhà phân phối được ủy quyền**: trong header/footer, logo
  luôn đi kèm dòng "Fast Group Engineering" ngay bên dưới, và footer luôn có dòng miễn trừ
  (biến `DISCLAIMER` trong `gen_lib.py`). File: `assets/brand/qlight-logo.png` (152×60, nền
  trong suốt, hiển thị 76×30). Không đặt logo Qlight một mình ở vị trí nhận diện của site.
- **Không host tài liệu của Qlight.** Trang model chỉ liên kết ra qlight.com cho
  catalog/manual/bản vẽ, cho tới khi xin được phép của hãng.

## Việc còn lại

- **C** — viết nội dung cho 159 hub + blog (khoảng 100.000 từ).
- **D** — bổ sung ảnh Certificate of Distributor vào `assets/images/` (xem tên file ở
  biến `COD_FILE` trong `gen_lib.py`); nếu chưa có, trang chủ tự chuyển sang khối chữ.
  Cân nhắc thêm: favicon riêng cho portal và ảnh OG mặc định (`assets/images/qlight-og.png`).
- **F** — thêm `Sitemap: https://fastgroup.vn/qlight-viet-nam/sitemap_index.xml` vào
  `robots.txt` gốc; thêm URL portal vào `sitemap.xml` gốc; rút gọn `brands/qlight.html`.
- **G → H → I → J** — publish, redirect Cloudflare, Search Console, bàn giao tên miền.
