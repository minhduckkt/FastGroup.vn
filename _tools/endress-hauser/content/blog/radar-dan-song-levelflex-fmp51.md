---
title: "Levelflex FMP51: Radar dẫn sóng TDR cho bồn hóa chất & đo interface"
slug: radar-dan-song-levelflex-fmp51
meta_title: "Radar dẫn sóng FMP51 TDR"
meta_description: "Levelflex FMP51 radar dẫn sóng (TDR): khi nào dùng thay radar không tiếp xúc, cách chọn probe rod/rope/coax, đo interface 2 lớp chất lỏng. Tư vấn & báo giá FastGroup."
primary_keyword: "radar dẫn sóng Levelflex FMP51"
secondary_keywords: ["Levelflex FMP51", "radar dẫn sóng TDR", "đo mức interface", "GWR vs radar", "chọn probe radar", "đo mức bọt hơi", "Endress+Hauser"]
brand: "Endress+Hauser"
category: "Đo mức - Radar dẫn sóng (Levelflex)"
source_docs: ["FA00001F00EN2726 (Level overview)", "endress.com – TI FMP51"]
---

# Levelflex FMP51: Radar dẫn sóng TDR cho bồn hóa chất & đo interface

Radar không tiếp xúc rất mạnh, nhưng có những tình huống nó "chào thua": bọt dày hấp thụ sóng, hơi đậm đặc gây tán xạ, chất có hằng số điện môi rất thấp phản xạ kém, hoặc cần đo **mặt phân cách hai lớp chất lỏng (interface)**. Đây là lúc **radar dẫn sóng (Guided Wave Radar – GWR)** như **Levelflex FMP51** phát huy: sóng đi dọc theo một que/dây dẫn nhúng vào môi chất, tập trung năng lượng nên ít bị môi trường phía trên làm nhiễu.

## GWR (TDR) hoạt động ra sao

FMP51 dùng nguyên lý **TDR (Time Domain Reflectometry)**: phát xung điện từ chạy dọc theo probe; khi gặp mặt phân cách môi chất (nơi hằng số điện môi thay đổi), một phần xung phản xạ về. Đo thời gian phản xạ → ra mức. Vì sóng "được dẫn" dọc probe thay vì phát tự do, GWR ít nhạy với bọt, hơi, bụi và hình học bồn phức tạp hơn radar không tiếp xúc.

## Thông số kỹ thuật quan trọng (theo tài liệu)

| Hạng mục | Giá trị (theo catalog/TI) |
|---|---|
| Nguyên lý | Radar dẫn sóng (TDR / GWR) |
| Dải đo | 10 m (rod) / 45 m (rope) / 20 m (coax) |
| Độ chính xác | ±2 mm / ±10 mm (tùy loại) |
| Nhiệt độ quá trình | -40 đến +200 °C |
| Áp suất quá trình | -1 đến +40 bar |
| Kết nối quá trình | Ren G/NPT ¾ & 1½" |
| Vật liệu tiếp xúc (probe) | 316L, Alloy C, ceramics (rope/rod/coax) |
| Tín hiệu / truyền thông | HART / PROFIBUS PA / FOUNDATION Fieldbus |
| Tùy chọn | Gastight feedthrough |

> Lưu ý biên tập: dải đo phụ thuộc loại probe; đo interface đòi hỏi điều kiện điện môi phù hợp giữa hai lớp. Cần đối chiếu TI đúng mã đặt hàng và xác minh khả năng đo interface cho cặp môi chất cụ thể.

## Chọn probe: rod / rope / coax

Đây là quyết định quan trọng nhất với GWR:

- **Rod (que cứng):** cho bồn nông–trung, chất sạch; cứng cáp, dễ vệ sinh.
- **Rope (dây):** cho bồn cao (tới 45 m); cần lực kéo và điểm neo; không dùng cho chất bám nặng dễ kéo lệch.
- **Coax (đồng trục):** hiệu năng tín hiệu tốt nhất, ít nhạy nhiễu và vật cản, phù hợp chất điện môi thấp — nhưng dễ tắc với chất bám/nhớt, cần môi chất sạch.

Nguyên tắc: chất sạch, cần độ nhạy cao, điện môi thấp → coax; bồn cao → rope; phổ thông → rod.

## Đo interface hai lớp — thế mạnh riêng

FMP51 có thể đo đồng thời **mức tổng** và **mặt phân cách** giữa hai lớp (ví dụ dầu/nước) — ứng dụng quan trọng trong tách dầu-nước, bình lắng. Điều kiện: lớp trên phải có điện môi đủ thấp và lớp dưới điện môi cao hơn, chênh lệch đủ để tạo hai phản xạ phân biệt. Đây là bài toán cần kiểm tra kỹ theo cặp môi chất.

## Khi nào chọn GWR thay radar không tiếp xúc

| Tình huống | Nên chọn |
|---|---|
| Bọt dày, hơi đậm đặc | **GWR (FMP51)** |
| Chất điện môi rất thấp | **GWR (coax)** |
| Cần đo interface | **GWR (FMP51)** |
| Bồn thoáng, bề mặt phẳng, cần không tiếp xúc | Radar (FMR) |
| Chất bám dính nặng lên probe | Radar không tiếp xúc |

## Kinh nghiệm lắp đặt & lỗi thường gặp

- **Chất bám trên probe:** GWR tiếp xúc môi chất nên chất bám gây sai số/echo giả — chọn probe phù hợp và vệ sinh định kỳ; không dùng coax cho chất bám.
- **Khoảng cách tới thành/vật cản:** rod/rope cần khoảng trống; tránh chạm thành.
- **Neo dây (rope):** cố định đầu dưới nếu có dòng chảy/khuấy mạnh để tránh đung đưa.
- **Vùng chết đầu/cuối probe:** mức quá sát mặt bích hoặc đáy probe kém chính xác — tính vào thiết kế.

## Ưu điểm, hạn chế, khi nào KHÔNG dùng

**Ưu điểm:** ít nhạy bọt/hơi, đo được điện môi thấp, đo interface, dải nhiệt/áp tốt. **Hạn chế/không phù hợp:** tiếp xúc môi chất nên không hợp chất bám nặng/kết tinh mạnh; probe dài trong bồn có khuấy mạnh cần neo; nếu ưu tiên hoàn toàn không tiếp xúc → radar FMR.

## Hiệu quả kinh tế (TCO)

GWR giải được các bài toán mà radar không tiếp xúc đo sai — tránh chi phí "mua rồi không dùng được". Khả năng đo interface trên cùng một thiết bị (thay vì hai phép đo) cũng tiết kiệm. Cần cân nhắc chi phí vệ sinh probe với chất bám khi tính tổng chi phí sở hữu.

## FastGroup hỗ trợ gì

FastGroup cung cấp thiết bị Endress+Hauser chính hãng tại Việt Nam. Với Levelflex FMP51, chúng tôi hỗ trợ: đánh giá chọn GWR vs radar không tiếp xúc, chọn probe rod/rope/coax theo môi chất, tư vấn bài toán đo interface, đối chiếu datasheet theo mã đặt hàng, hỗ trợ nhập khẩu và cung cấp CO/CQ theo từng đơn hàng.

## Kết luận & liên hệ

Khi bồn có bọt/hơi, môi chất điện môi thấp hoặc cần đo interface, Levelflex FMP51 là lựa chọn radar dẫn sóng đáng tin cậy. Để chọn đúng probe và nhận **báo giá chính hãng**, liên hệ FastGroup.

## Câu hỏi thường gặp (FAQ)

**1. Khi nào dùng GWR thay radar thường?** Khi có bọt/hơi nặng, điện môi thấp, hoặc cần đo interface.

**2. Chọn probe nào?** Rod cho phổ thông, rope cho bồn cao, coax cho chất sạch/điện môi thấp.

**3. Đo được dầu-nước không?** Có — đo interface nếu điện môi hai lớp phù hợp; cần kiểm tra theo cặp môi chất.

**4. Chất bám dính có ảnh hưởng không?** Có — GWR tiếp xúc môi chất; tránh coax với chất bám, vệ sinh định kỳ.

**5. Có đầy đủ CO/CQ không?** FastGroup cung cấp hàng chính hãng kèm CO/CQ và giấy tờ nhập khẩu theo từng đơn hàng.

## Nguồn tham khảo
- Endress+Hauser – Level measurement overview (FA00001F00EN2726)
- Endress+Hauser – Technical Information (TI) Levelflex FMP51, endress.com (đối chiếu theo mã đặt hàng)
