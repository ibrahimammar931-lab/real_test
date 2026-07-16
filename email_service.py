import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class EmailService:
    def __init__(self):
        self.smtp_server = 'smtp.gmail.com'
        self.smtp_port = 587
        self.from_email = 'your-email@gmail.com'
        self.password = os.environ.get('EMAIL_PASSWORD')
    
    def send_task_created_email(self, task):
        msg = MIMEMultipart()
        msg['From'] = self.from_email
        msg['To'] = 'recipient-email@gmail.com'
        msg['Subject'] = 'New Task Created'
        body = 'A new task has been created: ' + task['name']
        msg.attach(MIMEText(body, 'plain'))
        server = smtplib.SMTP(self.smtp_server, self.smtp_port)
        server.starttls()
        server.login(self.from_email, self.password)
        text = msg.as_string()
        server.sendmail(self.from_email, 'recipient-email@gmail.com', text)
        server.quit()