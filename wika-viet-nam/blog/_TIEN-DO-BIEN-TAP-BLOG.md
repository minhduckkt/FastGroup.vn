# Tiến độ biên tập Blog WIKA Việt Nam

Cập nhật: 2026-07-05 — **HOÀN THÀNH 34/34 bài**

## Mục tiêu
Làm giàu nội dung từng bài blog lên **1200–1600 chữ** (thêm ~400–800 chữ so với bản gốc), văn phong hấp dẫn, **cân bằng kỹ thuật + bán hàng**, và **chèn 1 ảnh minh họa** mỗi bài.

## Chuẩn đã áp dụng (giữ nguyên cho các bài sau)
- Chỉ chỉnh phần trong `<article class="article-body"> ... </article>`. Giữ nguyên head/schema, hero, related-products, footer.
- Cấu trúc: mở bài có "hook" → Tóm tắt nhanh → **figure ảnh** → các mục kỹ thuật (giữ bảng cũ, mở rộng) → 2–4 mục mới (ví dụ thực tế, sai lầm thường gặp, kinh nghiệm, so sánh) → FAQ (mở rộng) → CTA.
- Ảnh minh họa chèn dạng `<figure class="article-figure">` dùng 6 ảnh JPG sẵn có trong `assets/images/`:
  - `MW-140_9616_main.jpg` — đồng hồ áp suất (gauge)
  - `DMB-1-ES_2120870.jpg` — đồng hồ/hiển thị số (digital)
  - `DMU-1-ES_2129650.jpg` — cảm biến áp suất (transmitter)
  - `DRSEW-1-6-A20_2256476.jpg` — công tắc/cảm biến điện tử (switch)
  - `TSEW-50-A20_6858332.jpg` — thiết bị nhiệt độ (temperature)
  - `MAV-12-SMZ-MS_4568199.jpg` — van/phụ kiện (accessory/valve)
- Đường dẫn ảnh trong bài: `../../assets/images/<file>.jpg`
- Lưu ý: bài nhiều bảng thường phải thêm nhiều đoạn văn xuôi hơn mới đạt ≥1200 chữ (đếm theo khoảng trắng).
- Script mẫu: xem trong thư mục outputs của phiên (`enrich_batch*.py`, `extend_batch*.py`) — dùng regex thay khối article-body hoặc chèn trước `<h2>Câu hỏi thường gặp</h2>`.

## ĐÃ XONG (34/34) — tất cả đạt ≥1200 chữ (1202–1360), mỗi bài 1 figure ảnh, cấu trúc head/schema/hero/footer giữ nguyên

### Đợt 1 (12 bài đầu)
1. bao-gia-wika-nhanh-24h
2. bimetal-industrie-vs-chemie-an-mon
3. bo-dieu-khien-nhiet-do-gan-tu-digital
4. bo-hien-thi-4-20ma-gan-tu-panel
5. cach-doc-part-number-wika-nameplate
6. cam-bien-ap-suat-wika-4-20ma
7. cam-bien-giam-sat-luu-luong-flow-switch
8. cap-chinh-xac-dong-ho-ap-suat-class
9. checklist-thong-so-hoi-gia-dung-cu-do
10. chon-chan-dung-ngang-dong-ho-nhiet-do
11. chon-duong-kinh-mat-ren-dong-ho-ap-suat
12. chon-thiet-bi-do-ap-nhiet-dau-khi-og

### Đợt 2 (22 bài còn lại — vừa hoàn thành)
13. cong-tac-ap-suat-dien-tu-heavy-duty — DRSEW
14. dau-noi-chuyen-ren-reducer-adapter — MAV
15. do-chinh-xac-transmitter-02-05-span — DMU
16. dong-ho-ap-suat-dau-glycerin-vs-kho — MW-140
17. dong-ho-ap-suat-tiep-diem-contact-gauge — MW-140
18. dong-ho-ap-suat-wika-la-gi (gốc 859, cần nâng ≥1200) — MW-140
19. dong-ho-nhiet-do-luong-kim-bimetal-wika — TSEW
20. flush-diaphragm-transmitter-mang-phang — DMU
21. gioang-dong-ho-ap-suat-en837-din16258 — MAV
22. mua-dong-ho-wika-chinh-hang-o-dau — MW-140
23. nha-cung-cap-wika-epc-dau-khi — DMU
24. nhiet-ke-thuy-tinh-cong-nghiep-glass-thermometer — TSEW
25. ong-siphon-wassersackrohr-bao-ve-dong-ho — MAV
26. rtd-pt100-wika-2-3-4-wire — TSEW
27. safety-pattern-gauge-s3-en837 — MW-140
28. snubber-giam-xung-ap-dong-ho — MAV
29. temperature-transmitter-pt100-4-20ma — TSEW
30. thermowell-ong-bao-ve-nhiet-do-schutzrohr — TSEW
31. tieu-chuan-en-837-1-dong-ho-ap-suat — MW-140
32. tim-ma-thay-the-wika-cross-reference — DMB
33. van-chan-dong-ho-ap-suat-gauge-valve — MAV
34. wika-chinh-hang-viet-nam (gốc 824, cần nâng ≥1200) — MW-140

## GHI CHÚ SAU KHI HOÀN THÀNH
- **Ảnh hero:** các file `assets/images/hero/hero-*.webp` nay **đã có** (user đã thêm), hero blog không còn lỗi khi xem local.
- **Đường dẫn ảnh figure trong bài (22 bài đợt 2):** dùng chuẩn tự chứa `../../assets/images/<file>.jpg` (trỏ vào `wika-viet-nam/assets/images/`). An toàn khi deploy dưới `fastgroup.vn/wika-viet-nam/`.
- **Lưu ý cần rà (không bắt buộc):** 3/12 bài đợt 1 (`bao-gia-wika-nhanh-24h`, `bimetal-industrie-vs-chemie-an-mon`, `bo-dieu-khien-nhiet-do-gan-tu-digital`) dùng ảnh figure kiểu `../../../assets/images/wika_webp/*.webp` (trỏ ra ngoài site root). Ảnh vẫn hiện local nhưng nên đổi về chuẩn `../../assets/images/*.jpg` cho nhất quán/an toàn khi deploy. Hero + JSON-LG cũng đang dùng `../../../` và `//fastgroup.vn/assets/...` — nằm ngoài phạm vi biên tập bài, cần thống nhất khi deploy.
- **Hero trang chủ:** vẫn dùng `MW-140_9616_main.jpg` làm nền; có thể nâng cấp bằng ảnh hero mới nếu muốn.
