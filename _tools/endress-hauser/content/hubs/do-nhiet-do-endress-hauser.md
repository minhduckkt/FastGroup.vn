---
h1: "Thiết bị đo nhiệt độ Endress+Hauser — cảm biến, thermowell và transmitter iTEMP"
meta_title: "Thiết bị đo nhiệt độ Endress+Hauser | Fast Group"
meta_desc: "Chọn thiết bị đo nhiệt độ Endress+Hauser: nhiệt kế iTHERM và Omnigrad, thermowell, bộ chuyển đổi iTEMP TMT với 4-20mA, HART, PROFIBUS PA, FOUNDATION Fieldbus, PROFINET. RTD hay can nhiệt, cách chọn và lỗi hay gặp."
lead: "Một điểm đo nhiệt độ luôn gồm ba phần: phần tử cảm biến, ống bảo vệ và bộ chuyển đổi tín hiệu. Chọn đúng cả ba mới có phép đo bền — và trong thực tế, thermowell mới là chi tiết gây sự cố nhiều nhất."
eyebrow: "Endress+Hauser chính hãng · Đo nhiệt độ quá trình"
primary_keyword: "thiết bị đo nhiệt độ Endress+Hauser"
---

Đo nhiệt độ là phép đo phổ biến nhất trong nhà máy và cũng là phép đo hay bị xem nhẹ nhất. Một điểm đo nhiệt độ công nghiệp không phải một thiết bị đơn lẻ mà là một cụm ba phần: **phần tử cảm biến** (RTD hoặc can nhiệt), **ống bảo vệ thermowell** ngăn cách môi chất, và **bộ chuyển đổi tín hiệu** biến điện trở hoặc điện áp nhỏ thành tín hiệu chuẩn cho PLC/DCS.

## RTD Pt100 hay can nhiệt — chọn theo nhiệt độ và độ chính xác

**RTD (Pt100/Pt1000)** cho độ chính xác và độ ổn định dài hạn tốt hơn, tuyến tính hơn, dễ hiệu chuẩn. Đây là lựa chọn mặc định cho dải nhiệt độ quá trình thông thường của công nghiệp chế biến, thực phẩm, dược, nước.

**Can nhiệt (thermocouple, loại K/J/N/S…)** chịu nhiệt độ cao hơn nhiều, phản ứng nhanh hơn và bền cơ học hơn với rung động. Địa hạt của nó là lò nung, lò hơi, khói thải, luyện kim.

Ranh giới thực dụng: dưới khoảng 600 °C thì RTD gần như luôn tốt hơn nếu điều kiện cho phép; trên ngưỡng đó thì dùng can nhiệt. Với ứng dụng nhiệt độ rất cao, Endress+Hauser có dòng chuyên biệt như iTHERM TAF.

Về đấu dây RTD: **2 dây không dùng cho đo công nghiệp** vì điện trở dây dẫn cộng thẳng vào kết quả. **3 dây** là chuẩn phổ biến nhất và đủ cho hầu hết trường hợp; **4 dây** loại bỏ hoàn toàn ảnh hưởng dây dẫn, dùng khi cần độ chính xác cao nhất hoặc đường dây dài.

## Thermowell — chi tiết quyết định điểm đo có sống được không

Ống bảo vệ làm ba việc: ngăn môi chất tiếp xúc phần tử cảm biến, cho phép thay cảm biến mà không cần dừng quá trình, và chịu áp lực cùng lực dòng chảy.

Hai vấn đề kinh điển với thermowell:

**Cộng hưởng do dòng chảy (wake frequency).** Dòng môi chất chảy qua ống bảo vệ tạo xoáy luân phiên; nếu tần số xoáy trùng tần số riêng của ống, ống sẽ rung cộng hưởng và có thể gãy. Với đường ống có vận tốc dòng cao, cần tính toán kiểm tra theo ASME PTC 19.3 TW. Đây là hạng mục hay bị bỏ qua và hậu quả là ống gãy rơi vào đường ống.

**Chiều sâu nhúng không đủ.** Cảm biến cần được nhúng đủ sâu vào dòng để không bị dẫn nhiệt ra thành ống làm sai số. Quy tắc thực dụng là nhúng vượt qua lớp biên và đặt đầu ống ở vùng dòng chảy chính, tránh lắp vào đoạn ống chết hoặc ngay sát cút.

Ngoài ra, khe hở giữa cảm biến và lòng thermowell làm chậm đáp ứng đáng kể. Nếu quá trình cần đáp ứng nhanh, cần chọn ống thành mỏng, đầu thu nhỏ hoặc dùng vật liệu dẫn nhiệt lấp khe.

## Bộ chuyển đổi iTEMP — chọn theo giao thức của hệ thống

Tín hiệu thô từ RTD hay can nhiệt rất nhỏ và nhạy nhiễu, nên chuẩn công nghiệp là đặt bộ chuyển đổi ngay tại đầu đo. Dòng iTEMP TMT của Endress+Hauser chia theo giao thức đầu ra:

| Model | Đầu ra / giao thức | Ghi chú |
|---|---|---|
| TMT31 | 4–20 mA | Cấu hình qua Bluetooth |
| TMT36 | IO-Link | Cho hệ thống factory automation |
| TMT71 | 4–20 mA | Đầu nối dạng head mount |
| TMT72 | 4–20 mA HART | Chuẩn phổ biến nhất |
| TMT82 | HART, hai đầu vào | Dùng cho đo dự phòng / chênh lệch |
| TMT84 | PROFIBUS PA | |
| TMT85 | FOUNDATION Fieldbus | |
| TMT86 | PROFINET / Ethernet-APL | Hạ tầng mạng thế hệ mới |
| TMT142B, TMT162 | Lắp vỏ hiện trường | Có hiển thị, dùng khi cần đọc tại chỗ |

Phần lớn transmitter iTEMP nhận đầu vào đa năng (RTD, can nhiệt, mV, Ohm), nên cùng một model dùng được cho nhiều loại cảm biến — thuận lợi khi chuẩn hóa vật tư dự phòng trong kho.

**TMT82 hai đầu vào** đáng chú ý cho ứng dụng cần độ tin cậy cao: hai cảm biến trong cùng một thermowell, transmitter tự chuyển sang cảm biến dự phòng khi cảm biến chính hỏng, hoặc giám sát độ lệch giữa hai cảm biến để phát hiện trôi.

## Nhiệt kế theo ngành

Nhóm **iTHERM TM4xx** thiết kế cho vệ sinh: bề mặt nhẵn, không kẽ hở, kết nối clamp/hygienic cho thực phẩm, đồ uống và dược. Nhóm **iTHERM TM1xx và Omnigrad** là nhiệt kế công nghiệp đa dụng cho hóa chất, năng lượng, dầu khí. Ngoài ra có dòng tự hiệu chuẩn (TM371) tự kiểm tra điểm chuẩn ngay trong quá trình vận hành — giá trị lớn với ngành dược nơi hiệu chuẩn định kỳ tốn kém và phải dừng dây chuyền.

## Ba lỗi hay gặp

**Chọn dải đo quá rộng.** Transmitter được cấu hình theo dải; dải càng rộng sai số tuyệt đối càng lớn. Nên cài đúng dải làm việc thực tế thay vì để dải mặc định của cảm biến.

**Bỏ qua bù nhiệt độ điểm lạnh với can nhiệt.** Can nhiệt đo chênh lệch, nên điểm đấu nối phải được bù. Transmitter làm việc này, nhưng dây nối phải đúng loại dây bù tương ứng — dùng dây đồng thường là nguồn sai số phổ biến.

**Lắp cảm biến vào đoạn ống chết.** Nhiệt độ trong nhánh cụt không đại diện cho dòng chính. Lỗi này thường xuất hiện khi vị trí lắp được chọn theo tiện thi công thay vì theo quá trình.

## Fast Group hỗ trợ gì

Fast Group Engineering cung cấp thiết bị đo nhiệt độ **Endress+Hauser chính hãng tại Việt Nam**: tư vấn chọn RTD hay can nhiệt, cấu hình thermowell theo điều kiện dòng chảy, chọn transmitter theo giao thức hệ thống hiện hữu, đối chiếu datasheet đúng mã đặt hàng và hỗ trợ nhập khẩu kèm CO/CQ.

## Câu hỏi thường gặp

**Pt100 3 dây có đủ chính xác không?** Đủ cho hầu hết ứng dụng công nghiệp. Dùng 4 dây khi cần độ chính xác cao nhất hoặc khi đường dây tới transmitter dài.

**TMT84 và TMT85 khác nhau ở đâu?** TMT84 là PROFIBUS PA, TMT85 là FOUNDATION Fieldbus. Chọn theo giao thức mà hệ thống điều khiển của nhà máy đang dùng.

**Có cần thermowell không?** Trong đường ống có áp thì gần như luôn cần — vừa để bảo vệ cảm biến, vừa để thay cảm biến mà không phải dừng quá trình.

**Nhiệt kế tự hiệu chuẩn tiết kiệm được gì?** Giảm số lần phải tháo thiết bị đi hiệu chuẩn và giảm thời gian dừng dây chuyền. Đáng cân nhắc ở những điểm đo mà chi phí dừng máy cao hơn nhiều lần giá thiết bị.
