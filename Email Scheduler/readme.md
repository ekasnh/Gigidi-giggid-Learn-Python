Step 1: Install Required Packages
Make sure you have the necessary packages installed. If not, you can install them using pip:

pip install schedule

Step 2 

Run code.py 
 
Step 3: Set Up and Run the Script
Define Email Parameters:

Update the to_emails, from_email, smtp_server, smtp_port, login, password, and attachment_path variables with your own email details and report file path.
Schedule the Email:

Adjust the time in schedule.every().day.at("09:00").do(daily_report) to the desired time you want the email to be sent each day.
Run the Script:

Save the script in a .py file (e.g., daily_email_report.py).
Run the script using Python:

The script will now run continuously, checking every second if it needs to send the daily report. Make sure to keep the script running in an environment that is always on, like a server or a cloud instance.

Explanation
smtplib: Used to connect to the SMTP server and send the email.
MIME: Used to create the email message with attachments.
schedule: A lightweight scheduling library to run the report-sending function at a specific time daily.
while True loop**: Keeps the script running indefinitely, checking if it’s time to send the report.
Feel free to customize the script further according to your specific requirements!