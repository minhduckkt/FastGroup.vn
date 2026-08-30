---
title: "Prosonic FMU30: Cảm biến siêu âm đo mức nước & nước thải"
slug: cam-bien-sieu-am-prosonic-fmu30
meta_title: "Siêu âm FMU30 đo mức nước thải"
meta_description: "Prosonic FMU30 cảm biến siêu âm đo mức nước/nước thải: vùng mù, bù nhiệt độ, giới hạn khi có bọt-hơi, so sánh siêu âm vs radar. Báo giá chính hãng FastGroup."
primary_keyword: "cảm biến siêu âm đo mức FMU30"
secondary_keywords: ["Prosonic FMU30", "cảm biến siêu âm đo mức", "đo mức nước thải", "siêu âm vs radar", "đo lưu lượng mương hở", "vùng mù siêu âm", "Endress+Hauser"]
brand: "Endress+Hauser"
category: "Đo mức - Siêu âm (Prosonic)"
source_docs: ["FA00001F00EN2726 (Level overview)", "CP00022", "endress.com – TI FMU30"]
---

# Prosonic FMU30: Cảm biến siêu âm đo mức nước & nước thải

Ở các trạm bơm, bể chứa nước, mương hở hay hồ điều hòa, bài toán đo mức thường đi kèm ngân sách hạn chế và môi trường "bẩn": nước có váng, có rác, đôi khi có bọt. **Prosonic FMU30** là cảm biến siêu âm không tiếp xúc, kinh tế và bền, được nhiều đơn vị ngành nước và môi trường chọn cho các điểm đo phổ thông — nơi radar là "quá tay" còn phao thì hay kẹt.

## Nguyên lý siêu âm & vùng mù (blocking distance)

FMU30 phát xung siêu âm xuống bề mặt và đo thời gian phản hồi để tính khoảng cách → suy ra mức. Vì là sóng âm truyền trong không khí, tốc độ phụ thuộc nhiệt độ, nên thiết bị có **bù nhiệt độ** tích hợp để giữ độ chính xác. Một khái niệm bắt buộc phải hiểu là **vùng mù (blocking distance)**: khoảng ngay dưới mặt cảm biến mà sóng chưa "dội" về kịp — trong vùng này không đo được. Đây là nguyên nhân số một gây lỗi khi lắp: đặt cảm biến quá thấp khiến mức cao nhất rơi vào vùng mù.

## Thông số kỹ thuật quan trọng (theo tài liệu)

| Hạng mục | Giá trị (theo catalog/TI) |
|---|---|
| Nguyên lý | Siêu âm không tiếp xúc |
| Dải đo | 5 m (đầu 1½") / 8 m (đầu 2") |
| Độ chính xác | ±3 mm hoặc 0,12–0,2 % |
| Nhiệt độ quá trình | -20 đến +60 °C |
| Áp suất quá trình | +0,7 đến +3 bar |
| Kết nối quá trình | Ren G/NPT 1½" hoặc 2" |
| Vật liệu tiếp xúc | PP / EPDM |
| Tín hiệu | 4–20 mA HART |

> Lưu ý biên tập: dải đo (5 m/8 m) khác nhau theo cỡ đầu dò; vùng mù và độ chính xác phụ thuộc phiên bản. Cần đối chiếu TI đúng mã đặt hàng để lấy chính xác vùng mù và dải đo hữu ích.

Vật liệu **PP/EPDM** kháng hóa chất và nước thải tốt cho tầm giá; đây cũng là giới hạn nhiệt (đến +60 °C) — FMU30 không dành cho môi chất nóng.

## Ứng dụng tiêu biểu

- **Đo mức bể/giếng nước thải**, trạm bơm, hồ điều hòa.
- **Đo lưu lượng mương hở (open channel)** khi kết hợp với máng Parshall/đập tràn và đường đặc tính lưu lượng — một ứng dụng rất phổ biến trong ngành nước.
- Đo mức bồn hóa chất loãng áp suất thường.

## Siêu âm vs radar — chọn thế nào

Câu hỏi kinh điển. Kinh nghiệm chung:

- **Chọn siêu âm (FMU30)** khi: áp suất thường, không nhiều bọt/hơi, ngân sách hạn chế, môi trường sạch tương đối.
- **Chọn radar (FMR20B)** khi: có hơi nước/bụi/thay đổi nhiệt-ẩm mạnh (siêu âm dễ trôi), cần độ tin cậy cao hơn, hoặc bồn kín.
- Siêu âm **bị suy giảm nặng khi có bọt dày** (bọt hấp thụ sóng âm) hoặc hơi nước đậm đặc — đây là giới hạn cần cân nhắc ngay từ khâu chọn.

## Kinh nghiệm lắp đặt & lỗi thường gặp

- **Vùng mù:** lắp cảm biến đủ cao trên mức cao nhất để mức làm việc không rơi vào vùng mù.
- **Vuông góc mặt thoáng:** như radar, đầu dò cần nhìn thẳng xuống; nghiêng làm mất tín hiệu.
- **Tránh vật cản & thành:** ống, thang, dòng nước vào tạo phản xạ giả — dùng mapping để loại.
- **Nhiệt độ & nắng:** tránh ánh nắng trực tiếp gây gradient nhiệt sai lệch bù nhiệt; có thể dùng mái che.
- **Bọt/váng:** nếu quá trình sinh bọt nhiều, đây là dấu hiệu nên cân nhắc radar thay vì siêu âm.

## Ưu điểm, hạn chế, khi nào KHÔNG dùng

**Ưu điểm:** không tiếp xúc, kinh tế, dễ lắp, phù hợp nước/nước thải, hỗ trợ đo lưu lượng mương hở. **Hạn chế/không phù hợp:** bọt dày, hơi đậm đặc, áp/nhiệt cao, bồn kín áp lực — nên chuyển sang radar hoặc thủy tĩnh.

## Hiệu quả kinh tế (TCO)

FMU30 có chi phí đầu tư thấp và gần như không bảo trì cơ khí. Với điểm đo phổ thông đúng điều kiện làm việc, đây là lựa chọn tối ưu chi phí. Nhưng nếu môi trường có bọt/hơi, chọn siêu âm chỉ vì rẻ sẽ dẫn tới đo sai và tốn công xử lý — khi đó radar dù đắt hơn lại rẻ hơn về tổng thể.

## FastGroup hỗ trợ gì

FastGroup cung cấp thiết bị Endress+Hauser chính hãng tại Việt Nam. Với Prosonic FMU30, chúng tôi hỗ trợ: tư vấn chọn siêu âm vs radar theo điều kiện thực tế, tính vùng mù và chọn dải đo, hỗ trợ cấu hình đo lưu lượng mương hở, đối chiếu datasheet theo mã đặt hàng, hỗ trợ nhập khẩu và cung cấp CO/CQ theo từng đơn hàng.

## Kết luận & liên hệ

Cho đo mức nước/nước thải áp suất thường, Prosonic FMU30 là giải pháp siêu âm cân bằng chi phí và độ tin cậy — miễn là điều kiện không có bọt/hơi nặng. Để tư vấn chọn đúng và **báo giá chính hãng**, liên hệ FastGroup.

## Câu hỏi thường gặp (FAQ)

**1. FMU30 đo được bao xa?** 5 m với đầu 1½" và 8 m với đầu 2"; kiểm tra TI theo mã đặt hàng.

**2. Vùng mù là gì?** Khoảng ngay dưới đầu dò không đo được; phải lắp cao hơn mức cao nhất để tránh.

**3. Có đo được khi nhiều bọt không?** Bọt dày làm suy giảm mạnh tín hiệu siêu âm — nên cân nhắc radar.

**4. Đo lưu lượng mương hở được không?** Được, khi kết hợp máng/đập tràn và đường đặc tính lưu lượng.

**5. Có đầy đủ CO/CQ không?** FastGroup cung cấp hàng chính hãng kèm CO/CQ và giấy tờ nhập khẩu theo từng đơn hàng.

## Nguồn tham khảo
- Endress+Hauser – Level measurement overview (FA00001F00EN2726)
- Endress+Hauser – Technical Information (TI) Prosonic FMU30, endress.com (đối chiếu theo mã đặt hàng)
