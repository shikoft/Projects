# QR Code Generator

QR Code Generator là ứng dụng desktop được xây dựng bằng Python và PyQt, cho phép tạo mã QR từ nội dung văn bản hoặc đường link một cách nhanh chóng và trực quan.

---

## ✨ Tính năng

- Tạo mã QR từ text hoặc URL
- Tùy chỉnh màu QR
- Chèn logo vào giữa QR
- Chế độ Dark / Light
- Xuất file PNG
- Giao diện hiện đại (PyQt)

---

## 🖥 Ảnh giao diện

> (Bạn có thể thêm ảnh chụp màn hình ở đây)
>
> Ví dụ:
> ![Screenshot](screenshot.png)

---

## 🚀 Cách sử dụng

1. Mở `QR_Code_Generator.exe`
2. Nhập nội dung hoặc đường link
3. Nhấn **Tạo QR**
4. Nhấn **Lưu QR** để xuất file PNG

---

## 📦 Yêu cầu hệ thống

- Windows 10 / 11
- Không cần cài Python
- Không cần cài thư viện ngoài

---

## ⚙️ Build từ source

Nếu bạn muốn build lại ứng dụng:

```bash
pip install PyQt6
pip install qrcode[pil]
pip install pillow
pip install pyinstaller
