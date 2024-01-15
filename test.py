import smtplib
import socks

#socks.setdefaultproxy(TYPE, ADDR, PORT)
socks.setdefaultproxy(socks.SOCKS5, 'proxy.proxy.com', 8080)
socks.wrapmodule(smtplib)

smtpserver = 'smtp.live.com'
AUTHREQUIRED = 1 
smtpuser = 'example@hotmail.fr'  
smtppass = 'mypassword'  

RECIPIENTS = 'mailto@gmail.com'
SENDER = 'example@hotmail.fr'
mssg = "test message"
s = mssg   

server = smtplib.SMTP(smtpserver,587)
server.ehlo()
server.starttls() 
server.ehlo()
server.login(smtpuser,smtppass)
server.set_debuglevel(1)
server.sendmail(SENDER, [RECIPIENTS], s)
server.quit()