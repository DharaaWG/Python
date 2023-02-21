import smtplib
from email.message import EmailMessage
msg=EmailMessage()
msg['Subject']='mmm'
msg['From']='hhh'
msg['To']='191b096@juetguna.in'
with open ('textt.txt') as myfile:
    data= myfile.read()
    msg.set_content(data)
#msg.set_content("test email")
with smtplib.SMTP_SSL('smtp.gmail.com',465) as server:
    server=smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.login("dharaasharma02@gmail.com","dgzzyvnfdlqsflfx")
    server.send_message(msg)



#server.quit()
print('Email sent')

