import smtplib
from email.mime.text import MIMEText

SMTP_SERVER = "smtp.mail.yahoo.com"
SMTP_PORT = 465  # STARTTLS

EMAIL_ADDRESS = "sword.tyrant@yahoo.com"
APP_PASSWORD = "snow gloom fame debris present"  # 16-char app password

msg = MIMEText("Hello from Python using STARTTLS!")
msg["Subject"] = "Test Email"
msg["From"] = EMAIL_ADDRESS
msg["To"] = "sword.tyrant.error404@gmail.com"

with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
    #server.ehlo()
    #server.starttls()          # upgrade to TLS
    server.ehlo()
    server.login(EMAIL_ADDRESS, APP_PASSWORD)
    server.send_message(msg)

print("Email sent!")
