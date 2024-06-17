
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import schedule
import datetime


def send_email():
    # Email configurations
    sender_email = "test@test.com"
    receiver_email = "receive@GMAIL.COM"
    password = "PASSWORD"

    # Create message
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = "Daily Report - " + datetime.datetime.now().strftime("%Y-%m-%d")

    # Add body to email
    body = "Write your report content here."
    message.attach(MIMEText(body, "plain"))

    # Connect to SMTP server and send email
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        print("Email sent successfully!")


# Schedule sending email every day at a specific time
schedule.every().day.at("08:00").do(send_email)

# Keep the script running
while True:
    schedule.run_pending()
