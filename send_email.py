from email.mime.base import MIMEBase
import smtplib
import ssl

from email.mime.text import MIMEText
from email.mime.base import MIMEBase

from email import encoders

PORT = 465
SMTP_SERVER_DOMAIN_NAME = "smtp.gmail.com"
SENDER_MAIL = "@gmail.com"
PASSWORD = ""
EMAILS = []

def send_email(video):
    msg = MIMEText('DETECTED PERSON, VIDEO ATTACHED')
    msg['Subject'] = "Detected Person from Camera"
    msg['From'] = None # get email
    msg['To'] = ', '.join(EMAILS) # get list of emails

    payload = MIMEBase('application', 'octate-stream')
    payload.set_payload((video).read())
    encoders.encode_base64(payload)
    payload.add_header('Content-Decomposition', 'attachment', filename='detected_video.mp4')

    msg.attach(payload)

    ssl_context = ssl.create_default_context()
    service = smtplib.SMTP_SSL(SMTP_SERVER_DOMAIN_NAME, PORT, context=ssl_context)
    service.login(SENDER_MAIL, PASSWORD)

    for email in EMAILS:
        service.sendmail(SENDER_MAIL, email, msg)
    service.quit()