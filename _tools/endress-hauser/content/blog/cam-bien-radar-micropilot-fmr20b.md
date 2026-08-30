---
title: "Micropilot FMR20B: Radar 80 GHz đo mức cho bể & bồn chứa"
slug: cam-bien-radar-micropilot-fmr20b
meta_title: "Cảm biến radar FMR20B 80GHz đo mức"
meta_description: "Đánh giá radar Micropilot FMR20B 80GHz: nguyên lý, dải đo, kinh nghiệm lắp đặt cho bể nước/bồn chứa và tư vấn chọn cấu hình, báo giá chính hãng tại Việt Nam."
primary_keyword: "cảm biến radar đo mức FMR20B"
secondary_keywords: ["radar 80GHz đo mức nước", "Micropilot FMR20B giá", "cảm biến mức bồn nước", "radar không tiếp xúc", "đo mức bể chứa", "Bluetooth SmartBlue", "mua Endress+Hauser Việt Nam"]
brand: "Endress+Hauser"
category: "Đo mức - Radar không tiếp xúc (Micropilot)"
source_docs: ["FA00001F00EN2726 (Level overview)", "CP00022 (Pressure/Level selection)", "endress.com – TI FMR20B"]
---

# Micropilot FMR20B: Radar 80 GHz đo mức cho bể & bồn chứa

Với người làm vận hành, bài toán quen thuộc nhất ở khu bể chứa không phải là "đo được hay không", mà là *đo có ổn định khi điều kiện thay đổi hay không*: nước dao động, có bọt, hơi nước bốc lên, thành bể bám cặn, hay cánh khuấy tạo nhiễu. Cảm biến siêu âm cũ thường "trôi" khi nhiệt độ và độ ẩm thay đổi, còn phao cơ thì kẹt. Đây chính là lý do dòng radar 80 GHz như **Micropilot FMR20B** (và biến thể FMR30B) được nhiều nhà máy chọn thay thế: đo không tiếp xúc, gần như miễn nhiễm với môi trường phía trên bề mặt.

## Vì sao radar 80 GHz? Ý nghĩa thực tế của "búp sóng hẹp"

Điểm mấu chốt của công nghệ 80 GHz nằm ở góc phát sóng (beam angle) rất hẹp so với radar 26 GHz đời cũ. Búp sóng hẹp nghĩa là chùm tín hiệu tập trung, ít "quét" trúng thành bể, gân tăng cứng, đường ống hay cánh khuấy — những vật thể vốn tạo ra tín hiệu giả khiến phép đo nhảy loạn. Trong thực tế vận hành, đây là khác biệt giữa một vòng đo phải "vật lộn" với mapping nhiễu và một vòng đo lắp lên là chạy.

FMR20B đo **không tiếp xúc**, nên phần điện tử không bao giờ chạm môi chất. Với nước sạch, nước thải, hóa chất loãng hay bồn chứa phụ trợ, đây là ưu thế lớn về tuổi thọ và bảo trì: không có bộ phận cơ khí mài mòn, không cần tháo ra vệ sinh định kỳ như phao.

## Thông số kỹ thuật quan trọng (theo tài liệu)

| Hạng mục | Giá trị (theo catalog/TI) |
|---|---|
| Nguyên lý | Radar không tiếp xúc, 80 GHz (FMWCW) |
| Dải đo | Đến **30 m** |
| Độ chính xác | **±2 mm** |
| Nhiệt độ quá trình | -40 đến +80 °C |
| Áp suất quá trình | -1 đến +3 bar |
| Kết nối quá trình | Ren G/NPT 1" & 1½", mặt bích DN50–DN150 / 2–6" |
| Vật liệu tiếp xúc (wetted) | PVDF |
| Tín hiệu / truyền thông | 2 dây, 4–20 mA HART; cấu hình qua **Bluetooth** (app SmartBlue) |

> Lưu ý biên tập: dải đo, độ chính xác và giới hạn áp suất/nhiệt độ **phụ thuộc phiên bản và cấu hình đặt hàng**. Trước khi chốt model, cần kiểm tra datasheet (TI) đúng mã đặt hàng của FMR20B/FMR30B trên endress.com.

Điểm đáng chú ý cho người mua: vật liệu tiếp xúc là **PVDF** — kháng hóa chất tốt, phù hợp nước thải và nhiều hóa chất loãng, nhưng đây cũng là giới hạn cần lưu ý với môi chất ăn mòn mạnh hoặc nhiệt độ cao (khi đó phải nhìn sang dòng process như FMR51). Việc cấu hình qua Bluetooth/SmartBlue rất có giá trị thực tế: kỹ sư đứng dưới đất, dùng điện thoại là cài đặt được, không cần trèo lên nóc bồn để bấm nút — an toàn hơn nhiều.

## Cách đọc datasheet & chọn cấu hình

Ba câu hỏi cần trả lời trước khi đặt hàng FMR20B:

1. **Chiều cao bồn và khoảng chết (blocking distance):** dải đo 30 m thừa cho hầu hết bể công nghiệp, nhưng luôn phải trừ vùng chết ngay dưới anten. Bồn thấp mà lắp sai vị trí sẽ mất dải đo hữu ích ở phần trên.
2. **Kết nối quá trình:** ren hay mặt bích? Bồn có sẵn cổ nối nào? Chọn sai ren là phải chế adapter, dễ rò và lệch tâm anten.
3. **Tín hiệu ra:** 4–20 mA HART là chuẩn phổ biến nhất, dễ đấu vào PLC/DCS hiện hữu.

## Kinh nghiệm lắp đặt & lỗi thường gặp

Trong thực tế, đa số sự cố radar không tiếp xúc đến từ **vị trí lắp**, không phải từ thiết bị:

- **Lắp quá sát thành bể:** dù búp sóng 80 GHz hẹp, đặt cảm biến sát vách vẫn dễ nhận tín hiệu phản xạ từ thành và mối hàn. Nên đặt cách thành một khoảng theo khuyến nghị trong hướng dẫn lắp đặt.
- **Anten không vuông góc mặt thoáng:** radar cần "nhìn thẳng" xuống bề mặt. Lắp nghiêng làm suy giảm tín hiệu phản hồi.
- **Bỏ qua mapping (khử nhiễu):** nếu trong bồn có vật cản cố định (thang, ống, cánh khuấy), nên chạy mapping khi bồn ở mức thấp để thiết bị ghi nhớ và loại các tín hiệu giả.
- **Lỗi ống đứng/nozzle quá dài, hẹp:** cổ nối quá dài hoặc gờ trong lòng nozzle tạo phản xạ ký sinh; nên vát mép và giữ nozzle ngắn.

Khi tín hiệu chập chờn, quy trình kiểm tra hợp lý là: xem echo curve qua app → xác định đâu là echo thật, đâu là nhiễu → chạy lại mapping → kiểm tra vị trí/độ vuông góc anten trước khi nghi ngờ thiết bị hỏng.

## Ưu điểm, hạn chế và khi nào KHÔNG nên dùng

**Ưu điểm:** không tiếp xúc, gần như không bảo trì; ít nhạy với bọt nhẹ, hơi, bụi so với siêu âm; độ chính xác ±2 mm tốt cho tầm giá; cấu hình Bluetooth an toàn.

**Hạn chế / điều kiện không phù hợp:** giới hạn áp suất (-1…+3 bar) và nhiệt độ (đến +80 °C) khiến FMR20B **không dành cho** bồn áp lực cao hay môi chất nóng — đó là địa hạt của FMR51/FMR54. Bề mặt có bọt dày đặc hoặc chất có hằng số điện môi rất thấp cũng làm giảm chất lượng echo; khi đó nên cân nhắc radar dẫn sóng (Levelflex FMP51).

## Hiệu quả kinh tế (TCO)

Sai lầm phổ biến là chọn thiết bị đo mức chỉ theo giá mua. Với một bể vận hành liên tục, chi phí thực nằm ở *thời gian dừng máy khi phép đo sai* và *công bảo trì*. Radar không tiếp xúc như FMR20B gần như không có chi phí bảo trì cơ khí, không cần thay thế bộ phận mài mòn — tổng chi phí sở hữu thường thấp hơn phao cơ hoặc siêu âm về dài hạn, dù giá mua ban đầu có thể nhỉnh hơn thiết bị rẻ tiền không thương hiệu.

## FastGroup hỗ trợ gì

FastGroup (FAST GROUP CO., LTD) cung cấp thiết bị **Endress+Hauser chính hãng tại Việt Nam**, hỗ trợ nhà máy, nhà thầu EPC và đơn vị tích hợp hệ thống. Với FMR20B/FMR30B, chúng tôi hỗ trợ: đối chiếu datasheet đúng mã đặt hàng, tư vấn chọn dải đo – kết nối – vật liệu theo ứng dụng thực tế, kiểm tra cấu hình và nguồn gốc sản phẩm, hỗ trợ nhập khẩu và cung cấp CO/CQ theo từng đơn hàng, cùng hỗ trợ kỹ thuật trước và sau bán hàng.

## Kết luận & liên hệ

Nếu bạn cần đo mức nước, nước thải hay hóa chất loãng ở bồn/bể áp suất thường, Micropilot FMR20B là lựa chọn radar 80 GHz cân bằng tốt giữa độ tin cậy, độ chính xác và chi phí. Để chọn đúng cấu hình theo bồn của bạn hoặc nhận **báo giá thiết bị chính hãng**, liên hệ FastGroup — chúng tôi sẽ đối chiếu datasheet và tư vấn cấu hình phù hợp.

## Câu hỏi thường gặp (FAQ)

**1. FMR20B đo được dải bao nhiêu mét?** Theo catalog, đến khoảng 30 m; con số chính xác phụ thuộc anten và cấu hình — cần kiểm tra TI đúng mã đặt hàng.

**2. FMR20B khác FMR30B thế nào?** Cùng nền tảng 80 GHz, khác ở kiểu kết nối/anten và một số tùy chọn; nên xem datasheet để chọn biến thể phù hợp bồn của bạn.

**3. Có dùng cho bồn áp lực không?** Không phù hợp cho áp suất cao (giới hạn khoảng -1…+3 bar). Bồn áp lực nên dùng dòng process (FMR51/FMR54).

**4. Có cấu hình được bằng điện thoại không?** Có — qua Bluetooth và app SmartBlue, không cần trèo lên bồn để thao tác.

**5. Thiết bị có đầy đủ CO/CQ không?** FastGroup cung cấp hàng chính hãng kèm CO/CQ và giấy tờ nhập khẩu theo từng đơn hàng.

## Nguồn tham khảo
- Endress+Hauser – Level measurement overview (FA00001F00EN2726)
- Endress+Hauser – Technical Information (TI) Micropilot FMR20B/FMR30B, endress.com (cần đối chiếu theo mã đặt hàng cụ thể)
