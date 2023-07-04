from c__init__ import sender_address,sender_pass,receiver_address,server,port

def mail_sent(subject1='subject', content1='content as string'):
  import smtplib
  from email.mime.multipart import MIMEMultipart
  from email.mime.text import MIMEText  
      
  #Setup the MIME
  message = MIMEMultipart()
  message['From'] = sender_address
  message['To'] = receiver_address
  message['Subject'] = subject1 
  mail_content = content1 
  message.attach(MIMEText(mail_content, 'plain'))
  
  #Create SMTP session for sending the mail
  session = smtplib.SMTP(server, port)
  session.starttls()
  session.login(sender_address, sender_pass)
  text = message.as_string()
  session.sendmail(sender_address, receiver_address, text)
  session.quit()
  print('Mail Sent')
  return

# mail_sent('subject','content as string')