---
h1: "Radar đo mức Micropilot — chọn tần số, anten và cấu hình cho đúng bồn"
meta_title: "Radar đo mức Micropilot Endress+Hauser | Fast Group"
meta_desc: "Hướng dẫn chọn radar đo mức Micropilot FMR: khác biệt 80GHz và 26GHz, chọn anten và kết nối, khoảng chết, mapping khử nhiễu, khi nào không nên dùng radar không tiếp xúc. Báo giá chính hãng tại Việt Nam."
lead: "Micropilot là dòng radar không tiếp xúc của Endress+Hauser, từ model compact cho bể nước tới radar process cho bồn áp lực và tank gauging. Chọn đúng chủ yếu nằm ở tần số, anten và kết nối quá trình."
eyebrow: "Endress+Hauser chính hãng · Radar không tiếp xúc"
primary_keyword: "radar đo mức Micropilot"
---

Radar không tiếp xúc đã trở thành lựa chọn mặc định cho đo mức chất lỏng, vì một lý do rất thực dụng: phần điện tử không bao giờ chạm môi chất, nên không có gì mài mòn, không có gì cần tháo ra vệ sinh định kỳ. Với bồn vận hành liên tục, đây là khác biệt lớn về tổng chi phí sở hữu so với phao cơ hay siêu âm.

Dòng Micropilot (ký hiệu FMR) phủ từ radar compact giá hợp lý cho bể nước tới radar process cho bồn áp lực và hệ tank gauging thương phẩm.

## 80 GHz và 26 GHz — khác biệt thật sự là gì

Điểm khác biệt nằm ở **góc phát sóng**. Tần số càng cao thì với cùng kích thước anten, búp sóng càng hẹp. Búp sóng hẹp nghĩa là chùm tín hiệu tập trung xuống mặt thoáng, ít quét trúng thành bồn, gân tăng cứng, thang, ống nhúng hay cánh khuấy — những vật thể tạo tín hiệu giả khiến phép đo nhảy loạn.

Hệ quả thực tế:

- **80 GHz** cho phép dùng anten nhỏ hơn (kết nối nhỏ hơn, rẻ hơn), lắp được vào bồn hẹp nhiều chi tiết, ít phải mapping. Đây là lý do các model đời mới như FMR20B, FMR43, FMR51, FMR62B đều là 80 GHz.
- **26 GHz** vẫn hoàn toàn dùng tốt cho bồn lớn, thoáng, ít vật cản, và có lợi thế ở một số môi chất bụi nặng.

Với hầu hết dự án mới, 80 GHz là lựa chọn hợp lý trừ khi có lý do cụ thể để chọn khác.

## Ba câu hỏi trước khi chọn model

**1. Bồn có áp và nhiệt độ bao nhiêu?** Đây là câu hỏi phân tách rõ nhất. Các model compact như FMR20B/FMR30B thiết kế cho bồn khí quyển và nhiệt độ thường — giới hạn áp suất và nhiệt độ của chúng khá hẹp. Bồn áp lực, hơi nóng hoặc môi chất nhiệt độ cao là địa hạt của dòng process FMR51/FMR52/FMR54 và các biến thể tương ứng.

**2. Anten loại nào và kết nối gì?** Anten thấu kính, anten hình nón, anten drop hay anten dạng phẳng cho ngành vệ sinh — mỗi loại đi với một dải kết nối quá trình khác nhau. Bồn đã có sẵn cổ nối nào là ràng buộc thực tế đầu tiên; chọn sai phải chế adapter, dễ rò và làm lệch tâm anten.

**3. Môi chất có ăn mòn hay yêu cầu vệ sinh không?** Vật liệu tiếp xúc quyết định ở đây. Model kinh tế thường dùng PVDF — kháng hóa chất tốt cho nước thải và hóa chất loãng, nhưng có giới hạn với môi chất ăn mòn mạnh hoặc nhiệt độ cao. Ngành thực phẩm và dược cần kết nối vệ sinh và bề mặt nhẵn, ví dụ FMR43 hoặc FMR62B.

## Khoảng chết và chiều cao bồn

Mọi radar đều có một vùng ngay dưới anten không đo được — khoảng chết (blocking distance). Với bồn cao thì không thành vấn đề, nhưng với bồn thấp, đặt cảm biến sai vị trí sẽ mất phần dải đo hữu ích ở đúng vùng quan trọng nhất.

Nguyên tắc: lấy chiều cao bồn, cộng chiều dài nozzle, trừ khoảng chết của model — phần còn lại mới là dải đo dùng được. Con số khoảng chết cụ thể phụ thuộc anten và cấu hình, cần đối chiếu datasheet (TI) đúng mã đặt hàng.

## Mapping — bước hay bị bỏ qua nhất

Nếu trong bồn có vật cản cố định (thang, ống, cánh khuấy, dầm), thiết bị sẽ nhận được cả phản xạ từ chúng lẫn phản xạ từ mặt thoáng. Mapping là bước cho thiết bị "chụp" lại các phản xạ cố định khi bồn ở mức thấp, để sau đó loại chúng ra khỏi tính toán.

Rất nhiều ca báo "radar nhảy loạn, chắc thiết bị lỗi" thực ra chỉ là chưa chạy mapping. Quy trình kiểm tra hợp lý khi tín hiệu chập chờn: xem đường cong echo qua app hoặc phần mềm → xác định đâu là echo thật, đâu là nhiễu → chạy lại mapping → kiểm tra vị trí và độ vuông góc của anten — rồi mới nghi ngờ thiết bị.

## Khi nào radar không tiếp xúc không phải lựa chọn tốt

- **Bọt dày và bền.** Lớp bọt hấp thụ và phân tán sóng; khi đó radar dẫn sóng [Levelflex](../radar-dan-song-levelflex/) hợp lý hơn.
- **Hằng số điện môi rất thấp** (một số dung môi, khí hóa lỏng nhẹ). Bề mặt phản xạ yếu làm echo mờ.
- **Bám dính nặng lên anten.** Môi chất đóng cặn lên anten làm suy giảm tín hiệu; cần chọn anten dạng phẳng hoặc có phương án làm sạch.
- **Chất rắn rời trong silo rất cao có bụi mù khi nạp.** Vẫn làm được nhưng cần chọn model và anten chuyên cho chất rắn.

## Cấu hình bằng Bluetooth — lợi ích an toàn thật

Các model đời mới cấu hình qua Bluetooth với ứng dụng SmartBlue. Điều này nghe như tiện nghi nhưng thực chất là vấn đề an toàn: kỹ sư đứng dưới đất dùng điện thoại để cài đặt và xem đường cong echo, thay vì trèo lên nóc bồn thao tác nút bấm. Với bồn hóa chất hoặc bồn ngoài trời trên cao, đây là khác biệt đáng kể.

## Fast Group hỗ trợ gì

Fast Group Engineering cung cấp radar đo mức **Micropilot Endress+Hauser chính hãng tại Việt Nam**: tư vấn chọn tần số, anten và kết nối theo kích thước bồn thực tế, đối chiếu giới hạn áp suất – nhiệt độ theo datasheet đúng mã đặt hàng, kiểm tra yêu cầu chứng nhận phòng nổ, hỗ trợ nhập khẩu kèm CO/CQ.

## Câu hỏi thường gặp

**FMR20B dùng được cho bồn áp lực không?** Không phù hợp. Model compact có giới hạn áp suất hẹp; bồn áp lực nên dùng dòng process như FMR51/FMR54.

**Radar có đo được chất rắn rời không?** Có, nhưng cần chọn model và anten chuyên cho chất rắn, và lưu ý bề mặt vật liệu rắn thường nghiêng nên vị trí lắp quan trọng hơn nhiều so với chất lỏng.

**Bao lâu phải bảo trì một radar không tiếp xúc?** Về cơ khí gần như không có gì để bảo trì. Việc cần làm định kỳ là kiểm tra anten có bị bám cặn không và xác nhận đường cong echo vẫn sạch.

**Cần cung cấp thông tin gì để được tư vấn model?** Chiều cao bồn, môi chất, nhiệt độ và áp suất làm việc, kết nối sẵn có trên bồn, và khu vực lắp đặt có yêu cầu phòng nổ hay không.
