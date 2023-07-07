# ESpam (Email Spamer)

### Languages: 
- [Vietnamese](README-VI.md)

## Author: Ryder3x

ESpam is a tool that allows you to send bulk emails to target addresses with the purpose of spamming a specific message. Please note that currently the tool only works with Gmail. Other email providers such as Outlook, Hotmail, Yahoo, and Proton will categorize the emails as "spam" and move them to the respective folder.

## 📜 Usage

Basic syntax:

```
-m <Victim Email> -n <Number of spam emails> -s <Subject of spam email> -c <Content of spam email> -t <Sender information> -r <Reply-to address>
```

Example:

```
-m victim_mail@example.com -n 10 -s THIS_IS_SUBJECT -c hello (you've been spammed) -t Entity -r someone@mail.com
```

Notes:
- `-m` is the email address that will be spammed (*required*).
- `-n` is the number of times to send the spam emails (limit of 100 emails per run) (*required*).
- `-s` is the subject of the spam email (leave blank to use the default subject).
- `-c` is the content of the email when sending, HTML can be used (leave blank to use the default value).
- `-t` is the text that will be displayed as the recipient's name (victim_mail@example.com), but you can customize it to appear more mysterious (can be left blank).
- `-r` is your email address for the victim to contact you back (can be left blank).

## ⚙️ Installation and Usage

### Installation

To install, follow these steps:

1. Clone the repository:

   ```shell
   git clone https://github.com/Ryder3x/Espam.git
   ```

### Using on Terminal

1. Navigate to the `ESpam` directory:

   ```shell
   cd ESpam
   ```

2. Run the `ESpam.py` file:

   ```shell
   python3 ESpam.py
   ```

### Using directly in Python environment

```python
import requests as r
exec(r.get("https://raw.githubusercontent.com/Ryder3x/Espam/master/ESpam.py").text)
```

**Note:**
- After completing the setup, you can use the provided example snippets to run the code as mentioned above (replace `victim_mail@example.com` with the email address you want to spam).
- If you send 100 emails in a single run, there may be a delay for all the emails to appear in the recipient's mailbox (typically, it takes around 3-4 minutes for all 100 emails to be displayed).
- Since this is the original source code, if you download and modify it to "increase the number of emails spammed per run," there is a high chance of getting your IP address blocked by SMTP servers.
- If you are concerned about IP blocking, consider using a VPN.
- For those using Python compilers on Android (e.g., Pydroid), make sure to switch the keyboard from Vietnamese to English to avoid any errors.

⚠️ **Important Notice:**
I take no responsibility for any penalties or disturbances caused by your use of this tool. The consequences depend on how you use it, so please consider before using it.
