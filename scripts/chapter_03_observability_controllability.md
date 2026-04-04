# Kịch bản Thuyết trình - Chương 03: Chèn Điểm Kiểm Thử

## Slide 20: Mở đầu Chương 3 (03_00_chapter.html)
- **Hành động:** 
  Dừng lại vài giây để chuyển ý, giọng điệu thay đổi rành mạch.
- **Lời thoại tham khảo:**
  "Chương 3: Tìm hiểu khái niệm Khả năng điều khiển và Quan sát."

***

## Slide 21: Chèn Điểm Quan Sát (03_01_insertion.html)
- **Hành động:** 
  Chỉ tay vào cột bên trái (Cải thiện), sau đó trỏ sang cột dồn kênh MUX (Chia sẻ).
- **Lời thoại tham khảo:**
  "Bước đầu tiên là Chèn Điểm Quan sát (hay Observability Insertion). 
  Thứ nhất, về lý thuyết, ta chủ động gắn thêm đường mạch ra ngoài làm Test Points để theo dõi các node logic ẩn.
  Thứ hai, nếu cứ mang từng dây một gắn ra chân vi mạch mãi thì sẽ hết mất chân I O. Do đó, người ta dùng bộ Dồn kênh MUX. Bằng cách dùng chân Chọn Địa chỉ Address, ta chỉ cần tốn 1 chân râu cho hàng vạn tín hiệu được quan sát."

***

## Slide 22: Chèn Điểm Điều Khiển (03_02_muxdemux.html)
- **Hành động:** 
  Chỉ tay vào hình cổng AND/OR, chuyển sang hình DeMUX.
- **Lời thoại tham khảo:**
  "Tương tự như Quan sát, ta thực hiện Chèn Điểm Điều khiển (Controllability Insertion).
  (1) Thay vì chỉ móc vào để nhìn, ta sẽ chèn thêm cổng AND/NAND để ép node đó về mức 0 khi cần. Hoặc chèn cổng OR/NOR để ép nó lên mức 1. Vô cùng quyền lực.
  (2) Tương tự tình huống về thiếu chân, ta xài bộ Phân kênh (DeMUX) để phân rẽ luồng tín hiệu kích đến vô số các Test Point thông qua chân Địa chỉ."

***

## Slide 23: Kỹ thuật Scan Nối Tiếp Cách Ly (03_03_isolated_scan.html)
- **Hành động:** 
  Nhìn sơ đồ cấu trúc Shift Register đẩy bit từng phần tử.
- **Lời thoại tham khảo:**
  "Tuy nhiên, nếu mạch quá lớn, bộ MUX/DeMUX kia sẽ vô cùng vĩ đại. Tốn kém quá! Từ đó, ý tưởng Isolated Serial Scan ra đời. Ta thay thế mạng lưới song song loằng ngoằng kia bằng một Dây chuyền dịch bit (Shift Register). 
  Thay vì cấp test vector ồ ạt, một chiếc Virtual Tester sẽ thong thả đẩy từng bit một vào cổng Serial In. Cách này đổi thời gian để lấy lại không gian thiết kế."

***

## Slide 24: Giảm chân điều khiển & Nạp Rút đồng thời (03_04_reduce_simul.html)
- **Hành động:** 
  Để hoạt ảnh chạy lúc minh họa dòng Token và lúc Push Down / Pull up dữ liệu.
- **Lời thoại tham khảo:**
  "Với bài toán lớn, để giảm chân điều khiển, ta dùng kỹ thuật Truyền Cờ (Token Passing) qua thanh ghi, mượn chu kỳ xung nhịp để tiết kiệm chân Rìa.
  Hơn nữa, nhờ kiến trúc thông minh, thanh ghi dịch này có thể vừa nhận dữ liệu đẩy vào song song để nạp mức logic (Parallel Load), vừa lấy mẫu trạng thái (Capture) và đẩy ra ngoài đường Serial Out để kiểm tra."

***

## Slide 25: Khái niệm cơ bản của SCAN Design (03_05_basic_scan_concept.html)
- **Hành động:** 
  Quan sát và đợi hoạt ảnh Tool thay thế con D-FF thành SD-FF. Mỉm cười.
- **Lời thoại tham khảo:**
  "Đó chính là tiền thân của SCAN Design hiện nay! Thay vì nối những thanh ghi phụ bên ngoài mạch, ta dùng chính những con Flip-Flops nội bộ của hệ thống tạo thành Scan Chain.
  Khi vận hành, chip sẽ có 2 mode: Mode thường để xài mạch bình thường, và Mode Scan để Dịch/Kiểm thử.
  Các bạn đừng quá lo lắng về việc đấu dây thủ công cực khổ này. Ngày nay, các phần mềm xịn sò như Synopsys DFT Compiler sẽ hoàn toàn tự động nhổ Flip-Flop thường đi và cấy Flip-Flop SCAN (SD-FF) vào mạch chỉ trong chớp mắt chỉ qua vài dòng code."
