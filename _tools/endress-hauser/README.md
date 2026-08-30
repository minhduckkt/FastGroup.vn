# Bộ sinh site — Endress+Hauser Việt Nam

Sinh toàn bộ `fastgroup.vn/endress-hauser-viet-nam/` (221 trang) từ dữ liệu catalog và các bài viết
trong thư mục này. **Không sửa tay file HTML đã sinh** — mọi thay đổi sẽ bị ghi đè ở lần build sau.

## Chạy nhanh

```powershell
cd "fastgroup.vn\_tools\endress-hauser"
python build.py          # sinh 221 trang (~2,5 giây)
python validate.py       # link, ảnh, JSON-LD, title/meta/canonical
python validate2.py      # sitemap, công cụ tra mã, thẻ bắt buộc, placeholder sót
```

Chỉ cần Python 3 (thư viện chuẩn). Riêng `make_hero_images.py` cần `pillow` và `numpy`.

## Pipeline đầy đủ

| Bước | Script | Khi nào cần chạy |
|---|---|---|
| 1 | `prepare_data.py --src "<thư mục dữ liệu gốc>"` | Khi `data/products_master.csv` đổi, hoặc bổ sung ảnh mới |
| 2 | `make_hero_images.py` | Sau bước 1, nếu có ảnh sản phẩm mới |
| 3 | `build.py` | Mỗi khi sửa nội dung, taxonomy hoặc template |
| 4 | `validate.py` + `validate2.py` | Trước khi commit |

Bước 1 đọc kho ảnh gốc (`eh-portal/images/`, `images/`, `images_level/`) nằm **ngoài repo** vì quá lớn.
Kết quả đã dẫn xuất (`data/*.json` và `endress-hauser-viet-nam/assets/products/`) thì được commit,
nên bước 1 và 2 chỉ cần chạy khi dữ liệu nguồn thay đổi.

## Cấu trúc

```text
_tools/endress-hauser/
├── build.py                 → điều phối, gọi các hàm sinh trang
├── prepare_data.py          → bước 1: gộp SKU trùng, dò và copy ảnh
├── make_hero_images.py      → bước 2: tách nền ảnh cho background hero
├── validate.py              → kiểm tra link, ảnh, JSON-LD, thẻ meta
├── validate2.py             → kiểm tra sitemap, tra mã, placeholder sót
├── taxonomy.py              → ★ 14 hub (4 lĩnh vực + 10 công nghệ) và ảnh đại diện
├── data_layer.py            → nạp và chuẩn hoá dữ liệu, gán sản phẩm vào hub
├── render_parts.py          → khối HTML dùng lại: bảng thông số, thẻ sản phẩm, FAQ
├── gen_pages.py             → sinh từng loại trang
├── gen_lib.py               → markdown rút gọn, header/footer, JSON-LD, tiện ích
├── content/
│   ├── hubs/*.md            → ★ 14 bài kỹ thuật của trang hub (≈16.500 từ)
│   └── blog/*.md            → ★ 41 bài blog nguồn, có front matter SEO
├── data/
│   ├── products_master.csv  → dữ liệu gốc, 171 dòng
│   ├── products_clean.json  → 160 SKU sau khi gộp trùng (dẫn xuất)
│   ├── image_map.json       → SKU → đường dẫn ảnh gốc (dẫn xuất)
│   ├── image_files.json     → SKU → tên file trong assets/products (dẫn xuất)
│   └── blog_plan.json       → kế hoạch 41 bài: từ khoá, liên kết nội bộ
└── backup/                  → bản gốc các file site mẹ trước khi chỉnh sửa
```

★ = file nên sửa khi muốn thay đổi nội dung.

## Muốn sửa gì thì sửa ở đâu

| Muốn thay đổi | Sửa file |
|---|---|
| Nội dung một trang hub | `content/hubs/<slug>.md` |
| Nội dung một bài blog | `content/blog/<slug>.md` |
| Thêm/bớt hub, đổi nhóm sản phẩm | `taxonomy.py` |
| Thông số một model | `data/products_master.csv` rồi chạy lại bước 1 |
| Bố cục, giao diện | `endress-hauser-viet-nam/assets/site.css` |
| Cấu trúc trang, JSON-LD | `gen_pages.py` |
| Thông tin công ty, liên hệ | phần đầu `gen_lib.py` |

## Quy ước bắt buộc giữ

- **Đường dẫn ảnh hero phải tuyệt đối**: `url('/endress-hauser-viet-nam/assets/hero/x.png')`.
  Trình duyệt phân giải URL tương đối trong biến CSS theo vị trí *file CSS*, không theo trang —
  dùng đường dẫn tương đối sẽ hỏng ở trang chủ và trang sâu 2 cấp.
- **Không công bố giá.** Chuyển đổi bằng RFQ; trang model luôn nhắc đối chiếu Technical Information
  theo đúng mã đặt hàng.
- **Trường trống thì để trống**, không suy đoán cho đầy bảng thông số.
