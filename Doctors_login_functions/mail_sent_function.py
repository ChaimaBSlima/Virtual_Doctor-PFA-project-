import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(mail_text, recipient_email , subject):

    sender_email = "xyz@gmail.com"
    sender_password = "I am not going to set my password on github :)"


    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    msg.attach(MIMEText(mail_text, 'plain'))
    
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(msg)
        server.quit()
        return("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")
        return("Failed to send email!")
