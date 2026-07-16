import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

class EmailService:
    def __init__(self, email_password):
        self.email_password = email_password
    
    def send_task_created_email(self, task_title, task_description, recipient_email):
        try:
            # Create message container - the correct MIME type is multipart/alternative.
            msg = MIMEMultipart('alternative')
            msg['From'] = 'your-email@gmail.com'
            msg['To'] = recipient_email
            msg['Subject'] = 'New Task Created: ' + task_title
            
            # Create the body of the message (a plain-text and an HTML version).
            body = 'A new task has been created: ' + task_title + '\nDescription: ' + task_description
            msg.attach(MIMEText(body, 'plain'))
            
            # Set up the SMTP server.
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(msg['From'], self.email_password)
            
            # Send the email.
            text = msg.as_string()
            server.sendmail(msg['From'], msg['To'], text)
            server.quit()
        except Exception as e:
            print('Error sending email: ' + str(e))