import smtplib
from email.mime.text import MIMEText

def send_alert():
    sender_email = "your_email@gmail.com"
    receiver_email = "alert_receiver@gmail.com"
    subject = "⚠️ Pacemaker Intrusion Detected!"
    body = "A potential hacking attempt was detected on a pacemaker device. Immediate action required!"

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = receiver_email

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, "your_password")  # Replace with your email password
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()
        print("Alert email sent successfully!")
    except Exception as e:
        print(f"Error sending alert: {e}")
