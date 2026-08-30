---
h1: "Bộ chuyển đổi tín hiệu nhiệt iTEMP — chọn theo giao thức và kiểu lắp"
meta_title: "Bộ chuyển đổi nhiệt độ iTEMP TMT | Fast Group"
meta_desc: "Bộ chuyển đổi nhiệt độ iTEMP TMT của Endress+Hauser: TMT31, TMT36 IO-Link, TMT72 HART, TMT82 hai đầu vào, TMT84 PROFIBUS PA, TMT85 FOUNDATION Fieldbus, TMT86 PROFINET APL, TMT162 vỏ hiện trường."
lead: "Tín hiệu thô từ RTD hay can nhiệt rất nhỏ và nhạy nhiễu. Bộ chuyển đổi đặt ngay tại đầu đo biến nó thành tín hiệu chuẩn — và giao thức đầu ra là tiêu chí chọn quan trọng nhất."
eyebrow: "Endress+Hauser chính hãng · iTEMP transmitter"
primary_keyword: "bộ chuyển đổi nhiệt độ iTEMP"
---

Một Pt100 cho tín hiệu là điện trở vài trăm ohm; một can nhiệt loại K cho vài chục microvolt trên mỗi độ. Kéo những tín hiệu đó đi hàng chục mét trong nhà máy đầy biến tần và động cơ là công thức cho sai số. Vì vậy chuẩn công nghiệp là đặt **bộ chuyển đổi ngay tại đầu đo** — trong đầu nối của cảm biến hoặc trong vỏ hiện trường sát bên.

Dòng iTEMP TMT của Endress+Hauser chia chủ yếu theo **giao thức đầu ra** và **kiểu lắp**.

## Bảng chọn theo giao thức

| Model | Đầu ra / giao thức | Đặc điểm đáng chú ý |
|---|---|---|
| TMT31 | 4–20 mA | Cấu hình qua Bluetooth, gọn và kinh tế |
| TMT36 | IO-Link | Cho hệ thống factory automation |
| TMT71 | 4–20 mA | Head mount, cấu hình đơn giản |
| TMT72 | 4–20 mA HART | Lựa chọn phổ biến nhất cho nhà máy quá trình |
| TMT82 | HART, hai đầu vào | Đo dự phòng, đo chênh lệch, phát hiện trôi |
| TMT84 | PROFIBUS PA | |
| TMT85 | FOUNDATION Fieldbus | |
| TMT86 | PROFINET / Ethernet-APL | Hạ tầng mạng thế hệ mới |
| TMT142B, TMT162 | 4–20 mA HART, vỏ hiện trường | Có màn hình đọc tại chỗ |

Lưu ý phân biệt hai model hay bị nhầm: **TMT84 là PROFIBUS PA**, **TMT85 là FOUNDATION Fieldbus**. Chọn theo giao thức mà hệ điều khiển hiện hữu của nhà máy đang chạy, không theo model quen tay.

## Đầu vào đa năng — lợi thế cho kho vật tư

Phần lớn transmitter iTEMP nhận đầu vào đa năng: RTD (Pt100, Pt1000, Ni), can nhiệt các loại, điện áp mV và điện trở Ohm. Một model dùng được cho nhiều loại cảm biến khác nhau.

Ý nghĩa thực tế: nhà máy có thể chuẩn hóa còn một hoặc hai mã transmitter dự phòng trong kho thay vì mỗi loại cảm biến một mã. Khi hỏng, kỹ thuật viên lấy ra, cài lại loại đầu vào và dải đo là xong.

## TMT82 hai đầu vào — khi độ tin cậy quan trọng

Model hai đầu vào mở ra ba cách dùng mà một đầu vào không làm được:

**Đo dự phòng (redundancy).** Hai cảm biến trong cùng một thermowell; nếu cảm biến chính hỏng, transmitter tự chuyển sang cảm biến phụ và báo cảnh báo. Vòng đo không mất tín hiệu, và việc thay thế có thể lên lịch thay vì xử lý khẩn cấp.

**Giám sát độ lệch (drift detection).** So sánh liên tục hai cảm biến; khi độ lệch vượt ngưỡng, thiết bị báo — cách phát hiện sớm cảm biến đang trôi trước khi nó gây ra lỗi vận hành.

**Đo chênh lệch nhiệt độ.** Ví dụ chênh lệch giữa đầu vào và đầu ra của một bộ trao đổi nhiệt, tính ngay trong transmitter thay vì tính ở PLC.

## Head mount hay field housing

**Head mount** (lắp trong đầu nối của cảm biến, dạng đĩa tròn DIN B): gọn nhất, rẻ nhất, không cần vỏ riêng. Đây là lựa chọn mặc định khi không cần đọc giá trị tại chỗ.

**Field housing** (TMT142B, TMT162): transmitter đặt trong vỏ riêng có màn hình, gắn trên thanh ray hoặc ống. Chọn khi:

- Cần đọc giá trị tại hiện trường mà không có đồng hồ hiển thị riêng.
- Đầu nối cảm biến ở vị trí nóng hoặc rung mạnh, cần tách phần điện tử ra chỗ mát hơn.
- Cần không gian cho đấu nối phức tạp hơn.

## Cấu hình dải đo — chi tiết ảnh hưởng độ chính xác

Transmitter được cấu hình theo một dải cụ thể, và sai số thường được tính theo phần trăm của dải đó. Cài dải rộng hơn nhu cầu thực tế là tự làm giảm độ chính xác.

Ví dụ: quá trình chạy từ 20 đến 80 °C nhưng transmitter để dải mặc định −200 đến 850 °C thì sai số tuyệt đối sẽ lớn hơn nhiều so với cài đúng dải làm việc. Đây là bước hay bị bỏ qua khi lắp đặt hàng loạt.

## Với can nhiệt: đừng quên dây bù

Can nhiệt đo **chênh lệch** giữa điểm nóng và điểm đấu nối, nên điểm đấu nối phải được bù nhiệt độ. Transmitter làm việc bù này, nhưng **dây nối từ can nhiệt tới transmitter phải là dây bù đúng loại** tương ứng với loại can nhiệt.

Dùng dây đồng thường thay dây bù là nguồn sai số kinh điển — và là sai số thay đổi theo nhiệt độ phòng nên rất khó truy vết.

## Fast Group hỗ trợ gì

Fast Group Engineering cung cấp bộ chuyển đổi nhiệt độ **iTEMP Endress+Hauser chính hãng tại Việt Nam**: tư vấn chọn model theo giao thức hệ thống hiện hữu, xác định kiểu lắp head mount hay field housing, cấu hình dải đo và loại đầu vào, đối chiếu datasheet đúng mã đặt hàng, hỗ trợ nhập khẩu kèm CO/CQ.

## Câu hỏi thường gặp

**TMT84 và TMT85 khác nhau ở đâu?** TMT84 là PROFIBUS PA, TMT85 là FOUNDATION Fieldbus. Đây là hai giao thức khác nhau, phải chọn đúng theo hệ thống điều khiển.

**Có cần transmitter khi PLC đọc trực tiếp được Pt100 không?** Module PLC đọc trực tiếp được, nhưng tín hiệu phải đi cả quãng đường trong nhà máy dưới dạng điện trở — nhạy nhiễu và nhạy điện trở dây. Với khoảng cách xa hoặc môi trường nhiễu, đặt transmitter tại đầu đo cho kết quả ổn định hơn nhiều.

**TMT82 có bắt buộc dùng hai cảm biến không?** Không. Dùng một cảm biến vẫn bình thường; đầu vào thứ hai là tùy chọn khi cần dự phòng hoặc đo chênh lệch.

**Cấu hình transmitter bằng gì?** Tùy model: Bluetooth qua ứng dụng, phần mềm qua giao tiếp HART, hoặc công cụ cấu hình chuyên dụng. Fast Group hỗ trợ xác định công cụ phù hợp theo model.
