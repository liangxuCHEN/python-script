 #-*- coding: utf-8 -*-
import smtplib
from email.MIMEText import MIMEText

SMTP_SERVER = 'smtp.163.com'
MAIL_FROM = 'chenliangxu68@163.com'
PW = '163$323428'

def send_mail(mail_to, subject, msg_txt):
    # Record the MIME types of both parts - text/plain and text/html.
    msg = MIMEText(msg_txt, 'html', 'utf-8')
    msg['Subject'] = subject
    msg['From'] = MAIL_FROM
    msg['To'] = mail_to
    server = smtplib.SMTP(SMTP_SERVER, 25)
    server.login(MAIL_FROM, PW)
    mailto_list = mail_to.strip().split(",")
    if len(mailto_list) > 1:
        for mailtoi in mailto_list:
            server.sendmail(MAIL_FROM, mailtoi.strip(), msg.as_string())
    else:
        server.sendmail(MAIL_FROM, mail_to, msg.as_string())
    server.quit()
    return True

mail_to = 'lchen@europely.com'
subject = u'log for restart the php-fpm from 旅游'
msg_txt = ""
file = 'message.txt'
with open(file, "rb") as f:
    first = f.readline()      # Read the first line.
    f.seek(-493, 2)
    while True:
        line = f.readline()       # Read last line.
        msg_txt += line + '<br>'
        if len(line)==0: # Zero length indicates EOF 
            break 
print msg_txt

print send_mail(mail_to, subject, msg_txt)