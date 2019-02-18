import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
 
 
fromaddr = "jvd330@gmail.com"
toaddr = "sderyck@gmail.com"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "FROM THE GUYS"
 
body = "CURRENT TEMP IS 75F"
msg.attach(MIMEText(body, 'plain'))
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "J123456!")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
# email
