import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
 
def send_mail(room, time, email, email_pwd): 
    fromaddr = email
    toaddr = "piruthua@stud.ntnu.no"
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Booket rom"
    
    body = "Har booket rom " + room + " i tidsrommet: " + time
    msg.attach(MIMEText(body, 'plain'))
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, email_pwd)
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()