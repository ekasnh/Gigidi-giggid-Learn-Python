import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import schedule
import time
from datetime import datetime

def send_email(subject, body, to_emails, from_email, smtp_server, smtp_port, login, password, attachment_path=None):
    # Create a multipart message
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = ', '.join(to_emails)
    msg['Subject'] = subject

    # Attach the body with the msg instance
    msg.attach(MIMEText(body, 'plain'))

    # Attach any file if specified
    if attachment_path:
        attachment = open(attachment_path, "rb")
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f"attachment; filename= {attachment_path}")
        msg.attach(part)

    # Create a secure SSL context and send the email
    with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
        server.login(login, password)
        text = msg.as_string()
        server.sendmail(from_email, to_emails, text)

def daily_report():
    # Define email parameters
    subject = "Daily Report - " + datetime.now().strftime("%Y-%m-%d")
    body = "Please find attached the daily report."
    to_emails = ["recipient@example.com"]
    from_email = "your-email@example.com"
    smtp_server = "smtp.example.com"
    smtp_port = 465
    login = "your-email@example.com"
    password = "your-email-password"
    attachment_path = "path/to/your/report.csv"  # Change this to the path of your report

    send_email(subject, body, to_emails, from_email, smtp_server, smtp_port, login, password, attachment_path)

# Schedule the script to run daily at a specific time
schedule.every().day.at("09:00").do(daily_report)  # Change the time as needed

if __name__ == "__main__":
    while True:
        schedule.run_pending()
        time.sleep(1)
