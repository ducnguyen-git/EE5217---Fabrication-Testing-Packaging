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


## Slide 45: Phương pháp Scan Phân Đoạn (05_03_partial_scan.html)
- **Hành động:** 
  Chỉ vào tỷ lệ Phần trăm ở biểu đồ vòng tròn Partial Scan.
- **Lời thoại tham khảo:**
  "Thế còn với các dòng vi mạch cực rẻ và cần tối ưu Silicon thì sao? Partial Scan (Scan Phân Đoạn) được sinh ra. Thuật toán phần mềm nội soi và chỉ gài MUX-FF vào những nút cổ chai trọng điểm nhất, tiết kiệm 95% diện tích so với Scan toàn phần."

***

## Slide 46: Nút thắt Cổ chai của 1 dây chuyền MUX-DFF (05_04_multiple_scan_intro.html - 1/2)
- **Hành động:** 
  Chỉ vào chuỗi mạch dài vòng vèo.
- **Lời thoại tham khảo:**
  "Bên cạnh diện tích, Test Time lại gặp cảnh bế tắc. Hãy tưởng tượng nhồi 1 triệu con Flip-flop vào đúng MỘT dây chuyền Scan duy nhất. Thời gian bơm dữ liệu Shift In và Shift Out cực kỳ lê lết. Điều này làm phình to chi phí thuê mướn Tester."

***

## Slide 47: Scan Đa Chuỗi Song song (05_04_multiple_scan_intro.html - 2/2)
- **Hành động:** 
  Chỉ tay vào mô hình nhiều ống Pipeline song song độc lập.
- **Lời thoại tham khảo:**
  "Giải pháp thiết yếu là Scan Đa Chuỗi (Multiple Scan). Kỹ thuật này bẻ gãy sợi dây cáp quá trướng thành hàng chục dây chuyền ngắn hơn. Chúng chạy đồng loạt song song với nhau. Thời gian lập tức giảm thiểu tỷ lệ thuận theo số nhánh. Tuy nhiên, kiến trúc này bắt buộc chip tốn thêm nhiều cực Test Pins."

***

