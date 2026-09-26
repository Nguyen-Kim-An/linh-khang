# Thiệp Cưới Online: Khang & Linh

Website thiệp cưới online cao cấp với màn hình mở thiệp chuẩn theo mẫu ZenLove.
- **Phong cách**: Bì thư trang nhã với hoa lá màu nước góc thiệp, con dấu sáp xanh ô-liu có trái tim, nền gradient rêu sẫm huyền bí đúng chuẩn mẫu gốc.
- **Tên cô dâu & chú rể**: Chú rể **Khang** & Cô dâu **Linh**.
- **Thông tin gia đình**:
  - Nhà gái: **Ông Nguyễn Kim Trường & Bà Trần Thị Thắng**
  - Nhà trai: **Bà Phùng Thị Ngọ**
- **Ngày cưới**: **Thứ Sáu, ngày 20 tháng 11 năm 2026** (Đồng bộ toàn bộ web và bộ đếm ngược thời gian thực).
- **Backend RSVP & Gửi Email**:
  - Máy chủ backend `server.py` chạy tại cổng `8080`.
  - Tự động tiếp nhận lời chúc và xác nhận tham dự qua API `POST /api/rsvp`.
  - Toàn bộ dữ liệu được lưu tức thì vào file `rsvp_submissions.json`.
  - Hỗ trợ gửi thông báo tới email **`linhntp0512@gmail.com`**.
    *(Để kích hoạt gửi thư tự động qua Gmail SMTP, chỉ cần đặt biến môi trường `SMTP_USER` và `SMTP_PASSWORD` của tài khoản gửi thư)*.

---

## 📁 Cấu trúc thư mục

```text
wedding/
│
├── index.html                   # Trang web chính (đã liên kết toàn bộ tài nguyên local)
├── raw_site.html                # Bản tải gốc tham khảo
├── README.md                    # Tài liệu hướng dẫn
│
└── assets/
    ├── audio/
    │   └── wedding-music.mp3    # Nhạc nền tiệc cưới (lãng mạn, tự phát khi click/scroll)
    ├── fonts/                   # Toàn bộ 23 font chữ (UTM, Imperial Script, Google Fonts...)
    ├── images/                  # Toàn bộ hình ảnh cô dâu chú rể, popup QR mừng cưới, decor, icon
    ├── js/                      # Thư viện core LadiPage runtime, hiệu ứng, countdown, popup
    └── css/                     # Toàn bộ CSS giao diện và Google Fonts offline
```

---

## 🚀 Cách mở và sử dụng

### Cách 1: Mở trực tiếp bằng trình duyệt
- Nhấp đúp chuột vào file [index.html](file:///d:/Download/wedding/index.html) để mở bằng bất kỳ trình duyệt nào (Chrome, Edge, Firefox, Cốc Cốc, Safari).

### Cách 2: Chạy qua Local Web Server
Đã khởi chạy sẵn local web server tại cổng `8080`. Bạn có thể truy cập ngay tại:
👉 **[http://localhost:8080/](http://localhost:8080/)**

*(Nếu cần khởi động lại server sau này, chỉ cần mở terminal tại thư mục này và gõ: `python -m http.server 8080`)*

---

## ✨ Các tính năng nổi bật đã được clone trọn vẹn:
1. **Màn hình Mở Thiệp Cưới (ZenLove Style)**:
   - Khi vừa vào trang, hiển thị tấm bì thư thiệp cưới trang nhã với con dấu sáp trái tim, thông tin lễ cưới của Khang & Linh.
   - Hỗ trợ cá nhân hóa tên khách mời thông qua link URL (ví dụ: `?to=Anh+Tuấn` hoặc `?guest=Gia+đình+bác+Hùng`).
   - Tone màu trang nhã: Nền bìa hồng phấn dịu mát, hoa lá màu nước 2 góc, chữ và nút màu xanh ô-liu trầm.
   - Khi bấm nút **"Mở thiệp"**: Bì thư lướt mở chuyển cảnh mượt mà, âm nhạc đám cưới lập tức tự động vang lên và đưa khách vào trang thiệp chính.
2. **Thiết kế chuẩn Mobile & Desktop**: Tối ưu hiển thị dọc thanh lịch, nền background hoa văn trải dài trên màn hình lớn.
3. **Nhạc nền đám cưới & Nút xoay điều khiển**: Tự động phát khi bấm mở thiệp / cuộn trang, kèm nút biểu tượng xoay góc trái bật/tắt âm lượng.
4. **Đồng hồ đếm ngược (Countdown)**: Đếm ngược ngày cưới trực quan thời gian thực.
5. **Popup Gửi Mừng Cưới & QR Code**: Nút "Gửi mừng cưới" kích hoạt popup thông tin tài khoản và mã QR ngân hàng quét trực tiếp.
6. **Popup Danh bạ / Liên hệ**: Nút mở danh bạ, sao chép số điện thoại hoặc gọi điện nhanh.
7. **Form gửi lời chúc & xác nhận tham dự (RSVP)**: Khách mời nhập tên, lời chúc và chọn xác nhận tham dự.
8. **Toàn bộ tài nguyên Offline**: Không lo lỗi ảnh hay font chữ bị mất khi server gốc gỡ link.
