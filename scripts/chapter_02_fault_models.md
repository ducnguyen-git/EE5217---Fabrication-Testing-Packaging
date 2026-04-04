# Kịch bản Thuyết trình - Chương 02: Mạch Khả Kiểm và Mô hình Lỗi

## Slide 11: Mở đầu Chương 2 (02_00_chapter.html)
- **Hành động:** 
  Nhấn mạnh trọng âm vào chữ "chưa hỏng".
- **Lời thoại tham khảo:**
  "Tiếp theo là Chương 2: Mô hình Huffman và Thiết kế mạch khả kiểm."

***

## Slide 12: Mô hình Huffman - Khái quát (02_01_huffman.html - 1/3)
- **Hành động:** 
  Chỉ tay vào hai khối tách biệt vòng FSM.
- **Lời thoại tham khảo:**
  "Mạch tuần tự (Sequential) thì Test rất khó. Nên huyền thoại David Huffman đề xuất phân rã nó: Ông chia mạch thành 2 khối tách biệt hoàn toàn. Một nửa là Logic Tổ hợp thuần túy (Combinational), và phần thân là các khối Nhớ Flip-Flop tạo thành vòng hồi tiếp."

***

## Slide 13: Vấn đề của Hộp Đen (02_01_huffman.html - 2/3)
- **Hành động:** 
  Chỉ vào chữ DARK BOX.
- **Lời thoại tham khảo:**
  "Bế tắc của mô hình này nằm ở việc: Mảng Flip-Flop nội bộ giống như một chiếc Hộp Đen bị khóa kín. Dữ liệu Test từ ngoài (PI) đưa vào thì bị Flip-Flop chặn lại, nằm lì bên trong nên ta gọi là Non-controllable."

***

## Slide 14: Cắt đứt vòng mạch (02_01_huffman.html - 3/3)
- **Hành động:** 
  Chỉ vào cây kéo cắt đứt liên kết.
- **Lời thoại tham khảo:**
  "Giải pháp táo bạo của Scan là dùng phần mềm máy tính (ATPG Tool) để cắt đứt các cái vòng lặp vô tận này ra. Lúc này, chân đưa tín hiệu vào FF được phù phép coi như là Ngõ ra giả (Pseudo-PO), còn chân truyền ra thì coi như Ngõ vào giả (Pseudo-PI)."

***

## Slide 15: Kiểm Thử Mạch Tổ Hợp (02_02_combinational_testability.html)
- **Hành động:** 
  Hướng đến thanh Coverage 100%.
- **Lời thoại tham khảo:**
  "Vì mớ bùi nhùi FSM đã bị tháo rã thành Mạch Tổ Hợp thuần tuý, phần cứng Tool bây giờ có thể quét Test Patterns siêu nhanh và dễ thở. Minh chứng là độ bao phủ gỡ điểm mù lỗi (Fault Coverage) dễ dàng phóng lên ngưỡng cực hạn 100%."

***

## Slide 16: Tại sao cần SCAN Design? (02_03_why_scan_design.html)
- **Hành động:** 
  Chỉ tay vào chuỗi Shift Register.
- **Lời thoại tham khảo:**
  "Nhưng thực tế làm sao có sợi dây vật lý nào nối vào các chân Pseudo-PO này? Đó là lý do ta phải chèn cấu trúc SCAN. Tool sẽ đính kết liên tục tất cả các cái hộp đen dời dạc lại thành một 'Đường Ống Chuyền' (Shift Register) khổng lồ, đem trạng thái vi mạch ra phơi sáng."

***

## Slide 17: Đánh Đổi - Nhược Điểm (02_04_tradeoffs.html - 1/2)
- **Hành động:** 
  Nói chậm lại, chỉ vào các gạch đầu dòng nhược điểm.
- **Lời thoại tham khảo:**
  "Kỹ thuật bá đạo này hiển nhiên có sự đánh đổi (Trade-offs) đắt giá. Để kết dây điện, ta tốn mảng diện tích Area Overhead lớn cỡ 15%. Tiêu thụ thêm chân kiểm thử (Test Pins) tại vỏ chip, và bị hao phí Delay thời gian."

***

## Slide 18: Đánh Đổi - Ưu Điểm (02_04_tradeoffs.html - 2/2)
- **Hành động:** 
  Chốt lại giá trị ở Ưu điểm.
- **Lời thoại tham khảo:**
  "Bỏ qua nhược điểm đó, đánh đổi mang giá trị sống còn với doanh nghiệp. Lợi ích thu về là Test Quality hoàn hảo. Nó giúp việc chuẩn đoán bới móc vi mạch hư dễ như trở bàn tay."

***

## Slide 19: Mô Hình Lỗi Logic (02_05_logic_fault_models.html)
- **Hành động:** 
  Chỉ vào 3 lỗi cơ bản.
- **Lời thoại tham khảo:**
  "Tóm lại, chuỗi mắt xích Scan ấy bắt được các mô hình lỗi nào của tự nhiên? Chúng bắt tốt Lỗi Kẹt (Stuck-at): khi dây bị đứt hàn dính mức 0/1. Lỗi chạm chập (Bridging Short Circuit), và Lỗi Trễ Timing Delay làm suy giảm vi phạm tần số nhịp Clock."
