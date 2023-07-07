# ESpam (Email Spamer)

### Ngôn ngữ:
- [Tiếng Anh](README.md)

## Tác giả: Ryder3x

ESpam là một công cụ cho phép bạn gửi hàng loạt email đến địa chỉ đích với mục đích spam một thông điệp cụ thể. Lưu ý rằng hiện tại công cụ chỉ hoạt động trên Gmail. Các hộp thư khác như Outlook, Hotmail, Yahoo, Proton sẽ đưa các email vào mục "thư rác".

## 📜 Cách sử dụng

Cú pháp cơ bản:

```
-m <Email Cần Spam> -n <Số lần gửi spam> -s <Tiêu đề gửi Mail spam> -c <Nội dung gửi Mail spam> -t <Thông tin người gửi> -r <Địa chỉ trả lời lại Mail spam>
```

Ví dụ:

```
-m victim_mail@example.com -n 10 -s ĐÂY_LÀ_SUBJECT -c xin chào (bạn đã bị spam) -t Entity -r someone@mail.com
```

Chú thích:
- `-m`: địa chỉ email sẽ bị spam (*không được để trống*).
- `-n`: số lần gửi email spam (giới hạn 1 lần chạy là 100) (*không được để trống*).
- `-s`: SUBJECT của email spam (để trống sẽ sử dụng Subject mặc định).
- `-c`: nội dung của email khi gửi, có thể sử dụng HTML (để trống sẽ sử dụng giá trị mặc định).
- `-t`: văn bản sẽ hiển thị tên người nhận email, nhưng bạn có thể tùy chỉnh để tạo sự huyền bí (có thể để trống).
- `-r`: địa chỉ email của bạn để người nhận có thể liên hệ lại (có thể để trống).

## ⚙️ Cài đặt và sử dụng

### Cài đặt

Để cài đặt, hãy thực hiện các bước sau:

1. Clone repository:

   ```shell
   git clone https://github.com/Ryder3x/ESpam.git
   ```

### Sử dụng trên Terminal

1. Di chuyển vào thư mục `ESpam`:

   ```shell
   cd ESpam
   ```

2. Chạy tệp `ESpam.py`:

   ```shell
   python3 ESpam.py
   ```

### Sử dụng trực tiếp trên môi trường Python

```python
import requests as r
exec(r.get("https://raw.githubusercontent.com/Ryder3x/ESpam/master/ESpam.py").text)
```

**Lưu ý:**
- Sau khi hoàn thành cài đặt, bạn có thể sử dụng các đoạn mã ví dụ trên để chạ

y code như đã được mô tả ở trên (thay thế `victim_mail@example.com` bằng địa chỉ email bạn muốn spam).
- Nếu bạn gửi 100 email trong một lần chạy, có thể sẽ có thời gian trễ để tất cả các email được hiển thị trong hộp thư của người nhận (thông thường, 100 email sẽ mất khoảng 3-4 phút để hiển thị hết).
- Vì đây là mã nguồn gốc, nếu bạn tải xuống và chỉnh sửa để "tăng số lượng email spam trong mỗi lần chạy", có nguy cơ bị máy chủ SMTP chặn địa chỉ IP của bạn.
- Nếu bạn lo ngại về việc bị chặn IP, hãy cân nhắc sử dụng VPN.
- Đối với những người sử dụng trình biên dịch Python trên Android (ví dụ: Pydroid), hãy chắc chắn thay đổi bàn phím từ tiếng Việt sang tiếng Anh để tránh lỗi.

⚠️ **Lưu ý:** 
Tôi không chịu trách nhiệm cho bất kỳ hành vi bị phạt hay gây rối, phá hoại của bạn sử dụng công cụ này. Hậu quả phụ thuộc vào cách bạn sử dụng, hãy cân nhắc trước khi sử dụng.
