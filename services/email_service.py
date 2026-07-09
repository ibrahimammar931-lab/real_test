import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class EmailService:
    def __init__(self):
        self.email_password = os.environ.get('EMAIL_PASSWORD')
        self.email_address = os.environ.get('EMAIL_ADDRESS')
        self.smtp_server = os.environ.get('SMTP_SERVER')
        self.smtp_port = int(os.environ.get('SMTP_PORT'))

    def send_task_created_email(self, task):
        msg = MIMEMultipart()
        msg['From'] = self.email_address
        msg['To'] = 'recipient@example.com'
        msg['Subject'] = 'New Task Created'
        body = f'Task {task.id} created: {task.name}'
        msg.attach(MIMEText(body, 'plain'))
        server = smtplib.SMTP(self.smtp_server, self.smtp_port)
        server.starttls()
        server.login(self.email_address, self.email_password)
        text = msg.as_string()
        server.sendmail(self.email_address, 'recipient@example.com', text)
        server.quit()