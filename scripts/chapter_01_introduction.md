# Kịch bản Thuyết trình - Chương 01: Giới Thiệu Chung

## Slide 3: Mở đầu Chương 1 (01_00_chapter.html)
- **Hành động:** 
  Dừng lại 2-3 giây để mọi người đọc câu trích dẫn, sau đó đọc dẫn dắt.
- **Lời thoại tham khảo:**
  "Đến với Chương 1. Như câu nói nổi tiếng của William A. Foster: *'Chất lượng không bao giờ là sự tình cờ...'*. Để tạo ra những vi mạch chất lượng, chúng ta không thể hy vọng mạch sẽ tự động chạy đúng, mà phải chủ động thiết kế để có thể kiểm soát được. Và đó là cốt lõi phương pháp Design for Testability."

***

## Slide 4: Khái niệm DFT (01_01_khai_niem.html)
- **Hành động:** 
  Nhấn mạnh bằng giọng đối với 2 từ khóa "Điều khiển" và "Quan sát".
- **Lời thoại tham khảo:**
  "Vậy DFT là gì? Design for Testability là kỹ thuật thêm cấu trúc phần cứng phụ trợ vào thiết kế. Thêm vào tốn diện tích, nhưng đổi lại: Giúp ta tiếp cận trực tiếp vào các nút tín hiệu giấu sâu bên trong vi mạch.
  Tựu chung lại, DFT giải quyết 2 bài toán: Làm sao để **điều khiển** mạch (Controllability) và **quan sát** được mạch (Observability)."

***

## Slide 5: Bối cảnh (01_02_background.html - 1/2)
- **Hành động:** 
  Chỉ vào biểu đồ chi phí.
- **Lời thoại tham khảo:**
  "Tại sao chúng ta lại cần DFT? Ngày nay, độ phức tạp của chip ngày càng cao, dẫn tới thời gian và chi phí sinh ra Test vector gia tăng vô tội vạ, làm cho chi phí sản xuất IC tăng tuyến tính theo biểu đồ."

***

## Slide 6: Vai trò của Scan (01_02_background.html - 2/2)
- **Hành động:** 
  Chỉ vào cái khiên rào chắn bảo vệ trên minh họa.
- **Lời thoại tham khảo:**
  "Để giải quyết bế tắc, ý tưởng vĩ đại của Scan Design là 'bẻ gãy' một phần của các mạch tuần tự đa trạng thái thành các khối tổ hợp rời rạc đơn giản hơn. Nó hoạt động như một tấm khiên bảo vệ, giúp giảm tải thuật toán sinh Test Pattern."

***

## Slide 7: Mục tiêu 1 (01_03_objectives.html - 1/3)
- **Hành động:** 
  Chỉ vào mục tiêu đảm bảo chất lượng.
- **Lời thoại tham khảo:**
  "Do đó, chúng ta có 3 mục tiêu Test trọng tâm: Mục tiêu số 1 là Đảm bảo chất lượng sản phẩm xuất xưởng - chắc chắn được việc loại bỏ các vi mạch chết yểu trước khi đến tay người dùng."

***

## Slide 8: Mục tiêu 2 (01_03_objectives.html - 2/3)
- **Hành động:** 
  Lướt qua mục tiêu sản xuất.
- **Lời thoại tham khảo:**
  "Mục tiêu số 2 là Cải thiện tiến trình sản xuất (Yield Improvement). Bằng cách chạy các mẫu kiểm thử Scan, ta khoanh vùng được mask quang khắc nào ở xưởng đúc Wafer đang bị lỗi bụi, từ đó điều chỉnh."

***

## Slide 9: Mục tiêu 3 (01_03_objectives.html - 3/3)
- **Hành động:** 
  Chỉ vào hình Tester.
- **Lời thoại tham khảo:**
  "Cuối cùng, Scan Design làm chớp nhoáng quá trình đẩy dữ liệu, giúp chi phí thuê những cỗ máy ATE khổng lồ được suy giảm, tối ưu hóa Test Cost cho nhà máy."

***

## Slide 10: Khái quát một số lỗi Vật Lý (01_04_physical_defects.html)
- **Hành động:** 
  Chỉ tay vào 3 hình ảnh chụp hiển vi SEM trên màn hình.
- **Lời thoại tham khảo:**
  "Đây là một vài ví dụ rất trực quan về lỗi vật lý trên phiến silicon. (1) Là chiếc Transistor bị lủng màng oxide. (2) Bụi kim loại làm ngắn mạch chập chao. (3) Hoặc đứt liên kết mạch do dòng electron tàn phá (electromigration). Và các cấu trúc DFT Scan mà nhóm chuẩn bị trình bày sinh ra là để phát hiện chính xác những bệnh đó!"
