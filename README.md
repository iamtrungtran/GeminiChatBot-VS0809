# 🤖 GeminiChatBot-VS0809

Một ứng dụng Chatbot thông minh được tích hợp mô hình ngôn ngữ lớn **Google Gemini API**, giúp phản hồi người dùng một cách nhanh chóng, tự nhiên và chính xác. Dự án được thiết kế tối giản, dễ dàng cài đặt và mở rộng cho các mục đích học tập hoặc tích hợp hệ thống thực tế.

---

## 🚀 Tính năng nổi bật

- ⚡ **Phản hồi thời gian thực:** Kết nối trực tiếp với API Google Gemini (hỗ trợ các phiên bản Flash/Pro) mang lại tốc độ xử lý ưu việt.
- 💬 **Giao diện thân thiện:** Thiết kế trực quan, dễ tương tác, hỗ trợ hiển thị tốt trên cả máy tính và điện thoại.
- ⚙️ **Cấu hình linh hoạt:** Thay đổi tham số điều chỉnh mô hình (Temperature, TopK) và API Key dễ dàng qua biến môi trường.
- 📦 **Mã nguồn tối ưu:** Cấu trúc thư mục được tổ chức sạch sẽ, dễ đọc, phù hợp cho việc bảo trì hoặc phát triển thêm tính năng mới.

---

## 🛠️ Yêu cầu hệ thống

Trước khi bắt đầu cài đặt, hãy đảm bảo máy tính của bạn đã chuẩn bị sẵn các công cụ sau:
- **Python** (Phiên bản 3.9 trở lên) 
- Trình quản lý gói đi kèm: `pip`
- Một tài khoản Google để khởi tạo mã **Gemini API Key** (truy cập Google AI Studio để lấy mã miễn phí).

---

## 💻 Hướng dẫn cài đặt và chạy thử

Hãy làm theo tuần tự các bước sau để thiết lập dự án trên máy cục bộ của bạn:

Mở terminal hoặc command prompt trên máy và chạy lệnh:
```bash
git clone [https://github.com/iamtrungtran/GeminiChatBot-VS0809.git](https://github.com/iamtrungtran/GeminiChatBot-VS0809.git)
cd GeminiChatBot-VS0809
pip install -r requirements.txt
python main.py
