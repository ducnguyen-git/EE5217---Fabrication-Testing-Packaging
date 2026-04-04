# Kịch bản Thuyết trình - Chương 05: Các Kiến Trúc Scan

## Slide 43: Mở đầu Chương 5 (05_00_chapter.html)
- **Hành động:** 
  Chuyển nhẹ nhàng sang slide mới. Đọc trích dẫn với giọng suy ngẫm.
- **Lời thoại tham khảo:**
  "Chương 5: Các Kiến Trúc Scan mở rộng."

***

## Slide 44: Kiến Trúc Full Scan (05_01_full_scan_architecture.html)
- **Hành động:** 
  Chỉ vào đường SI nối SFF1 đến SFF3.
- **Lời thoại tham khảo:**
  "Đầu tiên là Full Scan, kiến trúc kinh điển và thuần chủng nhất: Lôi tất cả Flip-Flop nội bộ ra 'mux hoá' thành khối SFF và nối tiếp nhau. Điểm cộng mạnh mẽ nhất là cực kỳ thân thiện với các Tool EDA nhúng Code tự động."

***

## Slide 45: Nhược điểm của Full Scan (05_02_shadow_register.html - 1/3)
- **Hành động:** 
  Nhấn mạnh cụm '+120ps Delay' ở chỗ MUX.
- **Lời thoại tham khảo:**
  "Nhưng đáng tiếc Full Scan có điểm yếu cốt tử là gây hiện tượng chậm trễ Timing ngay trên đường truyền hệ thống gốc do cổng MUX cản trở dữ liệu."

***

## Slide 46: Khắc phục bằng Shadow Register (05_02_shadow_register.html - 2/3)
- **Hành động:** 
  Chỉ vào Data System tốc độ cao và cụm FF dự bị ở dưới.
- **Lời thoại tham khảo:**
  "Giải pháp sang chảnh đưa ra là Thanh ghi Bóng (Shadow Register). Thiết kể chủ trương giữ nguyên đường điện không có cổng MUX cản trở. Ta nuôi thêm một dàn thanh ghi 'hậu bị' chuyên làm nhiệm vụ Copy lén lại trạng thái FSM bị lỗi mà không hề chạm đến hệ thống gốc."

***

## Slide 47: Đánh đổi của Thanh ghi Bóng (05_02_shadow_register.html - 3/3)
- **Hành động:** 
  Lật lại và nhấn mạnh diện tích chip tăng.
- **Lời thoại tham khảo:**
  "Tất nhiên, sự sang chảnh này đánh đổi bằng gấp đôi diện tích thiết kế. Nhưng trên khía cạnh hiệu năng, mạch được bảo toàn Zero Delay Penalty cực kỳ quý giá cho vi xử lý siêu tốc độ."

***

## Slide 48: Phương pháp Scan Phân Đoạn (05_03_partial_scan.html)
- **Hành động:** 
  Chỉ vào tỷ lệ Phần trăm ở biểu đồ vòng tròn Partial Scan.
- **Lời thoại tham khảo:**
  "Thế còn với các dòng vi mạch cực rẻ và cần tối ưu Silicon thì sao? Partial Scan (Scan Phân Đoạn) được sinh ra. Thuật toán phần mềm nội soi và chỉ gài MUX-FF vào những nút cổ chai trọng điểm nhất, tiết kiệm 95% diện tích so với Scan toàn phần."

***

## Slide 49: Nút thắt Cổ chai của 1 dây chuyền MUX-DFF (05_04_multiple_scan_intro.html - 1/2)
- **Hành động:** 
  Chỉ vào chuỗi mạch dài vòng vèo.
- **Lời thoại tham khảo:**
  "Bên cạnh diện tích, Test Time lại gặp cảnh bế tắc. Nếu nhồi 1 triệu con Flip-flop vào đúng MỘT dây chuyền Scan duy nhất, thời gian bơm dữ liệu Shift In và Shift Out cực kỳ lê lết làm phình to chi phí thuê mướn Tester."

***

## Slide 50: Scan Đa Chuỗi Song song (05_04_multiple_scan_intro.html - 2/2)
- **Hành động:** 
  Chỉ tay vào mô hình nhiều ống Pipeline song song độc lập.
- **Lời thoại tham khảo:**
  "Giải pháp thiết yếu là Scan Đa Chuỗi (Multiple Scan / Parallel Arrays). Bẻ gãy sợi cáp quá trướng thành hàng chục dây chuyền ngắn chạy đồng luật song phôi với nhau. Thời gian lập tức giảm thiểu tỷ lệ thuận theo số nhánh, nhưng chip lại tốn thêm nhiều Test Pins trên tấm Board."

***

## Slide 51: Các Phương Pháp Khác (05_05_other_scan.html)
- **Hành động:** 
  Trỏ tay điểm qua sơ lược LSSD và RAS.
- **Lời thoại tham khảo:**
  "Cuối cùng, bên cạnh chuẩn MUX-DFF, thế giới DFT còn tồn tại LSSD của hãng IBM sở hữu hai chân Clock riêng biệt tránh kẹt Timing. Hay một kỹ thuật tối tân mang tên Random Access Scan (RAS) truy xuất lỗi ngẫu nhiên y như đọc RAM bộ nhớ nhúng."
