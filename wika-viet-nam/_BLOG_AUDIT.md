# Audit Blog WIKA — Lệch dữ liệu sản phẩm & bản Đức/Asia

**Ngày:** 2026-07-10 · Phạm vi: 34 bài blog trong Folder 4 · **32/34 bài bị ảnh hưởng**

## 1. Vấn đề gốc

Blog được viết theo **dòng mã Asia/Việt Nam cũ** (MW-140, DMU-1ES, DMB-1ES, DRSEW, TSEW, MSS, MANO, MAV, WSR). Nhưng **catalogue 301 sản phẩm trên site dùng mã quốc tế/Đức** (232.50, 213.53, A-10, CPG1500, PSD-4, PGS23.100, 910.xx, TG54...).

**Hệ quả:** đọc giả đọc blog thấy "WIKA MW-140" rồi tra trên site → **không có sản phẩm nào**. Autocomplete, tra mã, internal link đều lệch → mất chuyển đổi RFQ và giảm điểm SEO (nội dung không khớp catalogue).

Không phát hiện giá EUR/€ trong blog (tốt). Các thuật ngữ Đức trong slug (Wassersackrohr, Schutzrohr) và tiêu chuẩn EN 837 / DIN 16258 là **hợp lệ, nên giữ** (thể hiện gốc Đức, tốt cho E-E-A-T).

## 2. Bảng thay thế đề xuất (mã Asia → mã thật có trang trên site)

| Mã trong blog | Chức năng | Mã thật đề xuất | Trang sản phẩm | Số bài dính |
|---|---|---|---|---|
| **MW-140 / MW 140** | Đồng hồ áp suất Bourdon vỏ inox | **232.50** (hoặc 213.53) | `/san-pham/wika-232-50/` | 9 |
| **DMU-1ES** | Cảm biến / transmitter áp suất | **A-10** (hoặc S-20) | `/san-pham/wika-a-10/` | 10 |
| **DMB-1ES** | Đồng hồ áp suất số | **CPG1500** | `/san-pham/wika-cpg1500/` | 2 |
| **DRSEW** | Công tắc áp suất điện tử | **PSD-4** | `/san-pham/wika-psd-4/` | 2 |
| **TSEW** | Đồng hồ / công tắc nhiệt độ | **TG54** (dial) hoặc SC15 | `/san-pham/wika-tg54/` | 6 |
| **MSS** | Đồng hồ áp suất tiếp điểm | **PGS23.100** | `/san-pham/wika-pgs23-100/` | 5 |
| **MANO / MAV / WSR** | Van, siphon, phụ kiện | **910.11** (siphon) / 910.xx | `/san-pham/wika-910-11/` | 5 |

## 3. Ảnh minh họa cũng thuộc dòng Asia

Figure trong blog dùng ảnh: `MW-140_9616_main.jpg` (11 lần), `TSEW-50-A20` (6), `MAV-12-SMZ-MS` (5), `DMU-1-ES` (5), `DRSEW-1-6-A20` (2), `DMB-1-ES` (2). → Nên thay bằng ảnh của model thật tương ứng (đã có sẵn trong `assets/products/`).

## 4. Điểm cần chú ý theo bài (ví dụ điển hình)

- **`cach-doc-part-number-wika-nameplate`**: cả ví dụ đọc nameplate xây trên "DMU-1ES, 0…25 bar, 4–20mA" — cần đổi sang một model thật (VD A-10) để ví dụ khớp thực tế.
- **`dong-ho-ap-suat-wika-la-gi`**: câu chủ đề "WIKA MW 140 — dòng ống Bourdon vỏ inox" → đổi sang 232.50.
- **`tim-ma-thay-the-wika-cross-reference`**: nên dùng chính bộ mã thật làm ví dụ cross-reference.

## 5. Hai phương án xử lý

**A. Thay mã theo bảng + relink + đổi ảnh (khuyến nghị):** tự động thay mã Asia → mã thật trong 32 bài, chèn link tới trang sản phẩm thật, đổi ảnh figure sang model tương ứng. Nhanh, nhất quán, khớp catalogue.

**B. Chỉ báo cáo:** giữ nguyên, anh tự chỉnh theo bảng.

> Lưu ý: một số bài dùng mã Asia như *ví dụ dạy cách đọc* — thay mã đơn thuần vẫn đúng ngữ cảnh vì mã thật cũng minh họa được cùng khái niệm. Trường hợp cần viết lại sâu (rất ít) sẽ được đánh dấu riêng.

---

# ✅ ĐÃ XỬ LÝ (2026-07-10)

Đã áp dụng phương án **A** trên toàn bộ 34 bài: thay mã Asia → mã thật, relink sản phẩm, đổi ảnh figure.

## Kết quả kiểm tra sau sửa

| Chỉ số | Trước | Sau |
|---|---|---|
| Bài dính mã Asia | 32/34 | **0/34** |
| Mã "WIKA x" lệch catalogue | 22 loại | **0** (chỉ còn "EN 837-1" = tiêu chuẩn, giữ đúng) |
| Link sản phẩm trong blog | nhiều link gãy | **0 gãy**, 100% trỏ đúng SP thật |
| Ảnh figure | ảnh dòng Asia | ảnh model thật tương ứng |
| Thuật ngữ Pt100 / EN 837 | — | **giữ nguyên** (141 / 106 lần) |

## Bảng mã đã áp dụng (mở rộng)

| Nhóm | Mã Asia (gồm biến thể part-number) | → Mã thật |
|---|---|---|
| Đồng hồ áp suất inox/đổ dầu | MW-140, MW-163, MS-140/163/180/1100, MSK, MSF | **232.50** |
| Cảm biến/transmitter áp suất | DMU-1ES, DMU-1-FB, DMUB-1/10-ES | **A-10** |
| Đồng hồ áp suất số / chỉ thị số | DMB-1ES, DI-32-1 | **CPG1500** |
| Công tắc áp suất điện tử | DRSEW-1/10, DRSEW-1-6-A20 | **PSD-4** |
| Đồng hồ áp suất tiếp điểm | MSS-1100/1160, MWK | **PGS23.100** |
| Van / phụ kiện | MAV-12/14, MANO(S/F), RN-MANO, DR-14/18-MANO, DAA-4 | **910.11** |
| Ống siphon | WSRK-1212, WSRU-1212, WSR | **910.15** |
| Đồng hồ nhiệt độ cơ | TSEW-50-A20, TST | **TG54** |
| Công tắc nhiệt độ | SWEW-12/14 | **SC15** |
| RTD Pt100 / cảm biến nhiệt | PT1003, PT1003WC, TR-63, TMUC, DTR-230, SITS | **TR10-A** |
| Thermowell (ống bảo vệ) | TW-3563100 | **TW10** |

## Lưu ý còn lại (khuyến nghị rà tay, mức độ thấp)

- **`safety-pattern-gauge-s3-en837`**: "MSS" được map → PGS23.100 (đồng hồ tiếp điểm). Nếu bài nhấn mạnh *safety pattern S3 solid-front*, cân nhắc đổi thủ công sang **232.30** (đồng hồ inox safety pattern) cho sát nghĩa hơn.
- **`DAA-4`**: map tạm → 910.11 (phụ kiện); nếu thực chất là diaphragm seal, có thể chỉnh sang mã màng (họ 990.xx) khi có.
- Nội dung chữ (dải đo, ren, thông số minh họa) vẫn giữ nguyên — đã kiểm tra khớp ngữ cảnh với model mới (VD "A-10, 0…25 bar, 4–20 mA, 2-wire" là đúng với A-10).
