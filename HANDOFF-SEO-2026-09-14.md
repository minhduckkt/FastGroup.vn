# BÀN GIAO — Dự án nội dung & liên kết nội bộ fastgroup.vn

**Ngày:** 14/09/2026 · **Máy:** desktop-4ih0c65 · **Trạng thái:** Giai đoạn 1 + 2 hoàn tất

> Tài liệu này để tiếp tục công việc ở một phiên Claude khác. Dán toàn bộ file này vào phiên mới trước khi yêu cầu làm tiếp.

---

## 1. Bối cảnh

Fast Group (Đặng Minh Đức, MST **0315555189**) vận hành `fastgroup.vn` làm site doanh nghiệp, kèm nhiều **website chuyên ngành riêng cho từng thương hiệu**. Mục tiêu của đợt làm việc này:

1. Kéo dài nội dung các trang sản phẩm trên `fastgroup.vn` (trước đó chỉ ~420 từ)
2. Tạo liên kết từ `fastgroup.vn` sang 3 site vệ tinh: `hansford.vn`, `norgren.com.vn`, `gfps.vn`
3. Làm việc đó **không tạo dấu vết PBN** — mô hình là corporate microsite network hợp pháp, công khai quan hệ sở hữu

## 2. Đường dẫn repo (trên máy desktop-4ih0c65)

| Site | Đường dẫn | Ghi chú |
|---|---|---|
| fastgroup.vn | `D:\20. Các website\Fastgroup.vn\Fast Group` | Static HTML + GitHub Pages, có `.git` |
| hansford.vn | `D:\20. Các website\hansford.vn\hansford-sensor` | ~430 URL |
| norgren.com.vn | `D:\20. Các website\Norgren\norgren.com.vn\Norgren.com.vn` | ~12.603 URL |
| gfps.vn | **CHƯA TÌM THẤY** | Xem mục 7 |

⚠️ `D:\20. Các website\Norgren.vn\` là **bản build cũ** (chưa có nhóm FRL/xy-lanh). Không sửa vào đó.

---

## 3. Nguyên tắc đã thống nhất — áp dụng cho mọi việc làm tiếp

### 3.1 Định vị thương hiệu (bắt buộc dùng đúng chữ)

| Thương hiệu | Cách ghi | Lý do |
|---|---|---|
| Hansford Sensors | **"nhà phân phối chính thức"** | Đã có thoả thuận miệng, chưa có giấy |
| Norgren | **"đại lý bán hàng chính hãng"** | Nhập hàng chính hãng về bán |
| GF Piping Systems | **"đại lý bán hàng chính hãng"** | Nhập hàng chính hãng về bán |

Không dùng "nhà phân phối" cho Norgren và GF.

### 3.2 Quy tắc đặt link sang site vệ tinh

| Quy tắc | Nội dung |
|---|---|
| Mật độ | Xem bảng theo độ dài bên dưới |
| URL đích | **Mỗi link một URL khác nhau** — tuyệt đối không 2 link cùng trỏ 1 trang |
| Homepage | Tối đa 1 link trỏ homepage vệ tinh, ưu tiên deep link |
| Anchor | Mô tả nội dung trang đích, đa dạng, **không** dùng exact-match kiểu "nhà phân phối X chính hãng" |
| Vị trí | Contextual trong thân bài. **Không** dựng block footer site-wide mới |
| `rel` | `target="_blank" rel="noopener"` — dofollow, không nofollow |

| Độ dài trang | Số link vệ tinh |
|---|---|
| < 800 từ | 1–2 |
| 800–1.500 từ | 3–4 |
| 1.500–2.500 từ | 5–7 |
| > 2.500 từ | tối đa 7–8 |

### 3.3 Tín hiệu thực thể (quan trọng hơn backlink)

Hai chiều phải khai nhất quán:

- Trên `fastgroup.vn`: `Brand.sameAs` → URL site vệ tinh
- Trên site vệ tinh: `Organization.sameAs` → `https://fastgroup.vn/`
- Cả hai đầu khai `taxID: "0315555189"`, `legalName: "Công ty TNHH Fast Group"`
- NAP chuẩn (dùng y hệt ở mọi nơi):
  - `150/41 Nguyễn Cư Trinh, Phường Cầu Ông Lãnh, TP. Hồ Chí Minh`
  - `51 Lê Văn Lộc, Phường Vũng Tàu, TP. Hồ Chí Minh`
  - `+84938888958` · `minhduc@fastgroup.vn`

❌ **Không bao giờ** khai `parentOrganization` trỏ tới hãng nước ngoài — đó là tuyên bố Fast Group là công ty con của hãng. Quan hệ đúng là `brand: { name: "<Hãng>", sameAs: "<site hãng>" }`.

---

## 4. Đã làm — fastgroup.vn

### 4.1 Ba trang brand mở rộng

| File | Trước | Sau | Link vệ tinh |
|---|---|---|---|
| `brands/hansford_sensor.html` | 420 từ | **2.126 từ** | 6 → hansford.vn |
| `brands/iminorgren.html` | 454 từ | **2.068 từ** | 7 → norgren.com.vn |
| `brands/gf.html` | 420 từ | **2.234 từ** | 7 → gfps.vn |

Mỗi trang bổ sung 5 module: bảng series/part number · ứng dụng theo ngành · hướng dẫn kỹ thuật · chứng từ & giao hàng · FAQ 6 câu. Thêm JSON-LD `WebPage` + `BreadcrumbList` + `Brand` + `FAQPage`.

Số liệu trong bảng lấy thật từ chính site vệ tinh (VD: GF Type 546 — 4.207 model; Norgren FRL — 4.009 mã; xy-lanh compact — 1.482 mã).

### 4.2 Link từ trang có authority cao nhất

| File | Section mới | Link |
|---|---|---|
| `index.html` | "Hệ thống website chuyên ngành" — nêu rõ MST 0315555189 | 3 |
| `brands.html` | "Tra cứu chuyên sâu" — mô tả khác, deep link khác | 3 |

Dùng lại component `.portal` / `.portal-grid` có sẵn nên hoà vào thiết kế site.

### 4.3 Ảnh (15 file mới trong `img/`)

| Nhóm | File | Dùng ở |
|---|---|---|
| Thumbnail sản phẩm | `hansford-hs100/104/105/107/150/160/170i/420/capsule.webp` | Cột đầu bảng series Hansford |
| Ảnh ngành | `hansford-ind-ximang/daukhi/nhietdien/bom/cang/khaikhoang.webp` | 6 card ngành |

Nguồn: `D:\20. Các website\hansford.vn\hansford-sensor\assets\images\` (products/ và blog/). Đã tối ưu: gốc ~1,9 MB → **304 KB**. Thumbnail 240×180 nền trắng, ảnh ngành 640×427 crop 3:2, WebP quality 82.

### 4.4 Sửa lỗi

| Lỗi | Sửa |
|---|---|
| **Logo footer bị kéo giãn** (442×40, tỉ lệ 11,04 thay vì 5,43) — có trên **toàn bộ ~77 trang** | Thêm `footer.site .foot-grid img { width: auto; max-width: 100%; }` vào `css/fastgroup.css` |
| Bảng Hansford ghi "Dòng LPS" (tên danh mục, không phải series) | Đổi thành **HS-420 (LPS)** — part number thật |
| GF: `tra-cuu.html` bị link 2 lần · Norgren: `tim-kiem-ma-norgren/` bị link 2 lần | Link thứ 2 đổi sang `gfps.vn/dong-san-pham/` và `norgren.com.vn/san-pham/` |
| 6 anchor quá ngắn ("van bi", "fittings & tubing"…) | Viết lại đủ ngữ cảnh |

### 4.5 CSS đã thêm vào `css/fastgroup.css` (chỉ append cuối file, không sửa dòng cũ)

`.spec-table-wrap` · `.spec-table` · `.table-note` · `.faq-list` · `.faq-item` · `.cert-note` · `.st-thumb` · `.value-card.vc-photo` · `.brand-figure` · fix logo footer

Cache-buster hiện tại: `fastgroup.css?v=20260914b` (đã bump trên 5 trang đã sửa; **các trang khác vẫn là `?v=20260615-mobile`** — CSS chỉ append nên không ảnh hưởng).

### 4.6 `sitemap.xml`

`lastmod` → `2026-09-14` cho 5 URL: `/`, `/brands.html`, `/brands/hansford_sensor.html`, `/brands/iminorgren.html`, `/brands/gf.html`

---

## 5. Đã làm — site vệ tinh

| Site | File | Thay đổi |
|---|---|---|
| hansford.vn | `index.html` | `sameAs` → `["https://fastgroup.vn/"]` · **gỡ `parentOrganization` sai** · `brand.sameAs` → hansfordsensors.com · sửa NAP (`150` → `150/41`) |
| hansford.vn | `about.html` | Như trên + sửa `Phường Thắng Tam` → `Phường Vũng Tàu` + **1 link ngược contextual** trong đoạn dưới H2 "Fast Group Engineering – Đối tác phân phối chính hãng tại Việt Nam" |
| norgren.com.vn | `index.html` | Node `Organization` trong `@graph`: thêm `legalName`, `taxID`, `address`, `areaServed`, `sameAs`, `brand` |
| norgren.com.vn | `fast-group-engineering/index.html` | **Thêm mới** block `Organization` JSON-LD (trang này trước đó không có schema nào) |

---

## 6. Hai vấn đề cần bạn quyết

### 6.1 norgren.com.vn có link footer site-wide

~12.603 trang đều có link footer về `fastgroup.vn`, anchor **"Fast Group Engineering"**.

Đánh giá hiện tại: **chấp nhận được, chưa cần gỡ** — vì anchor là tên công ty (attribution chuẩn), không phải từ khoá thương mại. Nếu anchor là "nhà phân phối Norgren chính hãng" thì phải gỡ gấp. Đã khai `sameAs` + `taxID` công khai nên không có gì che giấu.

**Chưa quyết:** giữ nguyên / gỡ link / đổi thành text không link.

### 6.2 `hansford.vn/partials/footer.html` là bom hẹn giờ

File partial này **có** link tới `fastgroup.vn`, nhưng các trang đã build thì **không**. Nếu rebuild bằng partial này, hansford.vn sẽ có ngay footer site-wide trên ~430 trang. Cân nhắc trước khi chạy build.

---

## 7. CÒN LẠI — việc cần làm tiếp

| # | Việc | Chi tiết | Mức ưu tiên |
|---|---|---|---|
| 1 | **Push + Request Indexing** | `git add/commit/push` trong `D:\20. Các website\Fastgroup.vn\Fast Group`, sau đó vào Search Console request indexing 5 URL ở mục 4.6 | Cao |
| 2 | **Schema cho gfps.vn** | **Chưa tìm thấy source folder.** Đã rà `D:\20. Các website\gfps\gfps_codex` (chỉ có assets/data/scripts/outputs xlsx — không phải site), `Norgren.vn` (site khác), `minhduc.github.io` (là plastigauge). Cần hỏi chủ sở hữu vị trí repo, hoặc Add folder trong Claude desktop. Sau đó áp đúng mục 3.3 | Cao |
| 3 | **`partners.html` hub** | Section "Hệ thống website chuyên ngành" gom tất cả site, mỗi site mô tả thật 2–3 câu + anchor là tên miền/tên site. Không dùng anchor thương mại | Trung bình |
| 4 | **Đồng bộ `/en/`** | 3 file `en/brands/hansford_sensor.html`, `en/brands/iminorgren.html`, `en/brands/gf.html` — dịch nội dung mới, giữ hreflang | Trung bình |
| 5 | Ảnh cho Norgren/GF | Repo Norgren có 815 ảnh nhưng đặt tên theo part number (`0880300000000000.webp`), khó map theo nhóm. GF chỉ có PDF catalogue + 8 banner vật liệu | Thấp |
| 6 | Nhân bản sang các trang brand còn lại | 28 trang `/brands/*.html` khác vẫn ~420 từ. Dùng đúng template ở mục 4.1 | Thấp |

---

## 8. Lệnh kiểm tra lại (chạy sau mỗi lần sửa)

```python
# Đếm từ, đếm link vệ tinh, kiểm JSON-LD, phát hiện URL trùng
import re, json, glob
from collections import Counter
for f in glob.glob('brands/*.html') + ['index.html','brands.html']:
    h = open(f, encoding='utf-8').read()
    t = re.sub(r'(?is)<(script|style|nav|footer|header)[^>]*>.*?</\1>', '', h)
    words = len(re.sub(r'\s+', ' ', re.sub(r'(?s)<[^>]+>', ' ', t)).split())
    ld = [json.loads(x) for x in
          re.findall(r'(?s)<script type="application/ld\+json">(.*?)</script>', h)]
    urls = re.findall(r'href="(https://(?:hansford\.vn|norgren\.com\.vn|gfps\.vn)[^"]*)"', h)
    dup = {k: v for k, v in Counter(urls).items() if v > 1}
    noalt = len(re.findall(r'<img(?![^>]*\balt=)[^>]*>', h))
    print(f'{f:34s} {words:5d} từ · jsonld {len(ld)} OK · link {len(urls)} '
          f'· TRÙNG {dup} · thiếu alt {noalt}')
```

Kiểm tra thêm bằng trình duyệt (Playwright/Chrome DevTools):
- Logo footer phải có tỉ lệ **5,43** (217×40), không phải 11,04
- Ở viewport 390px: `document.documentElement.scrollWidth === clientWidth`
- ⚠️ Nếu test local mà thiếu file ảnh, ảnh vỡ sẽ render theo thuộc tính `width` và báo tràn ngang **giả**. Phải có đủ ảnh mới đo được chính xác.

---

## 9. Kết quả kiểm tra lần cuối (14/09/2026)

| Hạng mục | Kết quả |
|---|---|
| Số từ | Hansford 2.126 · Norgren 2.068 · GF 2.234 |
| JSON-LD | 12/12 trên fastgroup.vn + 6/6 trên vệ tinh — parse hợp lệ |
| Cân bằng thẻ HTML | 0 thẻ thừa/lệch trên cả 5 trang |
| URL trùng | 0 |
| Ảnh thiếu `alt` | 0/36 |
| Mobile 390px | 5/5 trang không tràn ngang |
| `sitemap.xml` | XML hợp lệ |
| Logo footer | 217×40, tỉ lệ 5,43 ✅ |
