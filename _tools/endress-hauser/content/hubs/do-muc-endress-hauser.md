---
h1: "Thiết bị đo mức Endress+Hauser — chọn đúng nguyên lý trước khi chọn model"
meta_title: "Thiết bị đo mức Endress+Hauser | Fast Group"
meta_desc: "Hướng dẫn chọn thiết bị đo mức Endress+Hauser theo nguyên lý: radar 80GHz, radar dẫn sóng, siêu âm, thủy tĩnh, chênh áp, điện dung, servo và bức xạ. Cây quyết định, lỗi thường gặp và báo giá chính hãng."
lead: "Chín nguyên lý đo mức trong danh mục Endress+Hauser, mỗi nguyên lý mạnh ở một điều kiện quá trình khác nhau. Chọn đúng nguyên lý trước khi chọn model là bước quyết định độ bền của phép đo."
eyebrow: "Endress+Hauser chính hãng · Đo mức liên tục"
primary_keyword: "thiết bị đo mức Endress+Hauser"
---

Sai lầm tốn kém nhất trong một vòng đo mức không phải là chọn sai model, mà là **chọn sai nguyên lý đo**. Một cảm biến radar tốt lắp vào bồn có bọt dày sẽ vẫn cho tín hiệu chập chờn; một cảm biến thủy tĩnh chính xác vẫn sai số lớn nếu tỷ trọng môi chất thay đổi theo nhiệt độ. Khi nguyên lý đã sai, không có cấu hình nào cứu được.

Danh mục đo mức liên tục của Endress+Hauser phủ chín nguyên lý. Việc chọn bắt đầu từ câu hỏi môi chất và bồn trông thế nào, để dẫn về đúng nhóm sản phẩm.

## Chín nguyên lý đo mức và điều kiện mạnh của từng loại

| Nguyên lý | Dòng sản phẩm | Mạnh nhất khi | Yếu khi |
|---|---|---|---|
| Radar không tiếp xúc (80/26 GHz) | Micropilot FMR | Bồn chứa lỏng, nước thải, hóa chất; cần không tiếp xúc | Bọt rất dày; hằng số điện môi rất thấp |
| Radar dẫn sóng (TDR) | Levelflex FMP | Hằng số điện môi thấp, bồn hẹp, có bọt, có khuấy | Môi chất bám dính nặng lên que/cáp |
| Siêu âm | Prosonic FMU / FDU | Nước, nước thải, chất rắn rời; giá hợp lý | Hơi nước, bụi dày, chân không, nhiệt độ dao động mạnh |
| Thủy tĩnh (áp suất cột chất lỏng) | Deltapilot FMB, Waterpilot FMX | Giếng, bể hở, trạm bơm; lắp đơn giản | Tỷ trọng thay đổi; môi chất bám bít màng |
| Chênh áp | Deltabar FMD / PMD | Bồn kín có áp, tháp, nồi hơi | Cần 2 điểm trích áp; ống mao dẫn nhạy nhiệt |
| Điện dung | Liquicap FMI | Bồn nhỏ, môi chất dẫn điện ổn định | Môi chất thay đổi hằng số điện môi |
| Servo | Proservo NMS | Bồn thương phẩm cần độ chính xác cao nhất | Chi phí và bảo trì cơ khí |
| Radar tank gauging | Micropilot NMR | Bồn tồn trữ lớn, giao nhận hàng | Không dành cho bồn quá trình nhỏ |
| Bức xạ (gamma) | Gammapilot FMG | Không thể xuyên thành bồn bằng cách khác | Yêu cầu giấy phép nguồn phóng xạ |

Bảng trên chỉ để loại trừ nhanh. Con số dải đo, áp suất và nhiệt độ cụ thể của từng model **phải đối chiếu datasheet (TI) đúng mã đặt hàng** trên endress.com trước khi chốt.

## Cây quyết định: bốn câu hỏi loại trừ

**Câu 1 — Môi chất là lỏng hay rắn rời?** Chất rắn rời (xi măng, hạt nhựa, ngũ cốc, tro bay) loại ngay thủy tĩnh và chênh áp, vì cột vật liệu rắn không tạo áp suất tuyến tính theo chiều cao. Còn lại radar, radar dẫn sóng, siêu âm và bức xạ.

**Câu 2 — Bồn có áp và nhiệt độ cao không?** Bồn khí quyển ở nhiệt độ thường mở ra gần như mọi lựa chọn, kể cả các model kinh tế như FMR20B hay FMU30. Bồn áp lực hoặc môi chất nóng đưa lựa chọn sang dòng process: Micropilot FMR51/FMR54, Levelflex FMP54/FMP56, hoặc Cerabar/Deltabar với màng ngăn.

**Câu 3 — Bề mặt có bọt, có khuấy, có bụi không?** Đây là câu hỏi phân loại radar không tiếp xúc với radar dẫn sóng. Bọt dày và hằng số điện môi thấp làm suy giảm tín hiệu phản xạ của radar không tiếp xúc; radar dẫn sóng dẫn năng lượng dọc theo que hoặc cáp nên chịu được các điều kiện này tốt hơn nhiều. Đổi lại, que/cáp có tiếp xúc môi chất nên không dùng được cho chất bám dính nặng.

**Câu 4 — Cần độ chính xác thương phẩm hay chỉ cần kiểm soát vận hành?** Nếu số đo dùng để giao nhận hàng, tính tiền hoặc quyết toán tồn kho thì địa hạt là tank gauging: Proservo NMS8x hoặc Micropilot NMR8x. Nếu chỉ cần điều khiển bơm, cảnh báo tràn hay giữ mức trong khoảng, một radar compact là đủ và rẻ hơn nhiều lần.

## Đo mức liên tục và công tắc báo mức — đừng lẫn hai bài toán

Một nhầm lẫn phổ biến khi lập BOM là dùng thiết bị đo mức liên tục cho chức năng chống tràn hoặc chống chạy khô. Hai bài toán này khác nhau về bản chất an toàn:

- **Đo mức liên tục** trả về giá trị 4–20 mA theo chiều cao. Khi thiết bị lỗi, giá trị có thể "đứng" ở một mức trông hợp lý mà không ai biết.
- **Công tắc báo mức** chỉ trả về hai trạng thái, nhưng được thiết kế để phát hiện chính lỗi của mình — nguyên lý rung (vibronic) của Liquiphant tự giám sát tần số dao động, ăn mòn hay bám dính đều làm thay đổi tần số và thiết bị báo lỗi.

Vì vậy trong hầu hết nhà máy, mức tràn và mức cạn được bảo vệ bằng công tắc riêng, độc lập với vòng đo liên tục. Xem thêm nhóm [công tắc báo mức](../cong-tac-muc-endress-hauser/).

## Bốn lỗi lắp đặt làm hỏng phép đo tốt

**Lắp quá sát thành bồn.** Ngay cả radar 80 GHz búp sóng hẹp cũng nhận phản xạ từ vách, mối hàn và gân tăng cứng nếu đặt sát. Luôn giữ khoảng cách theo hướng dẫn lắp đặt của model.

**Nozzle quá dài hoặc quá hẹp.** Cổ nối dài và có gờ trong lòng tạo phản xạ ký sinh ngay vùng gần anten — vùng vốn đã là khoảng chết. Nozzle nên ngắn, vát mép, đúng đường kính khuyến nghị.

**Bỏ qua bước mapping.** Bồn có thang, ống nhúng, cánh khuấy thì phải chạy mapping (khử nhiễu) khi mức thấp để thiết bị ghi nhớ các phản xạ cố định. Rất nhiều ca "radar nhảy loạn" chỉ là chưa mapping.

**Đặt cảm biến ngay dưới dòng nạp liệu.** Dòng chảy rơi tạo bề mặt động và bọt cục bộ; đặt lệch khỏi vùng nạp là cách sửa rẻ nhất.

## Đọc cấu hình trước khi hỏi giá

Với thiết bị đo mức Endress+Hauser, ba thông tin quyết định phần lớn giá và lead time:

1. **Kết nối quá trình** — ren hay mặt bích, tiêu chuẩn và kích thước. Chọn sai là phải chế adapter, dễ rò và lệch tâm anten.
2. **Vật liệu tiếp xúc** — PVDF, 316L, Alloy hay phủ PTFE, quyết định bởi tính ăn mòn của môi chất.
3. **Chứng nhận phòng nổ** — ATEX/IECEx và cấp bảo vệ. Khu vực nguy hiểm bắt buộc, và đây là hạng mục hay bị quên trong BOM sơ bộ.

Khi gửi yêu cầu, nếu có sẵn chiều cao bồn, môi chất, nhiệt độ – áp suất làm việc và khu vực lắp đặt, Fast Group có thể đề xuất được 1–2 model kèm cấu hình thay vì hỏi lại nhiều vòng.

## Fast Group hỗ trợ gì

Fast Group Engineering cung cấp thiết bị đo mức **Endress+Hauser chính hãng tại Việt Nam** cho nhà máy, nhà thầu EPC và đơn vị tích hợp hệ thống: đối chiếu datasheet đúng mã đặt hàng, tư vấn chọn nguyên lý và cấu hình theo điều kiện quá trình thực tế, kiểm tra nguồn gốc, hỗ trợ nhập khẩu và cung cấp CO/CQ theo từng đơn hàng.

## Câu hỏi thường gặp

**Radar 80 GHz và 26 GHz khác nhau ra sao?** Tần số cao hơn cho búp sóng hẹp hơn, ít quét trúng vật cản trong bồn nên tín hiệu sạch hơn và lắp được vào bồn nhỏ, nhiều chi tiết. Dòng 26 GHz vẫn dùng tốt cho bồn lớn, ít vật cản.

**Bồn có bọt thì nên chọn gì?** Ưu tiên radar dẫn sóng Levelflex. Nếu bắt buộc không tiếp xúc, cần đánh giá độ dày và độ bền của lớp bọt trước khi chọn radar.

**Có bắt buộc lắp cả công tắc mức khi đã có đo liên tục không?** Về nguyên tắc an toàn, chức năng chống tràn và chống chạy khô nên độc lập với vòng đo liên tục. Yêu cầu cụ thể tùy tiêu chuẩn và đánh giá rủi ro của dự án.

**Fast Group có báo giá theo model hay theo cấu hình?** Theo cấu hình — cùng một model nhưng khác kết nối, vật liệu và chứng nhận thì giá và lead time khác nhau đáng kể.
