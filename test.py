import smtplib
import socks

#socks.setdefaultproxy(TYPE, ADDR, PORT)
socks.setdefaultproxy(socks.SOCKS5, '38.91.107.224', 80)
socks.wrapmodule(smtplib)

smtpserver = 's1.ct8.pl'
AUTHREQUIRED = 1 
smtpuser = 'admin@starbucks.com'  
smtppass = '#Null123#'  

RECIPIENTS = 'nulltype404@gmail.com'
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