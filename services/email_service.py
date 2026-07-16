import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
import logging

class EmailService:
    def __init__(self, smtp_server, smtp_port, from_email, password):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.from_email = from_email
        self.password = os.environ.get('EMAIL_PASSWORD')

    def send_task_created_email(self, task):
        try:
            msg = MIMEMultipart()
            msg['From'] = self.from_email
            msg['To'] = task.assignee_email
            msg['Subject'] = 'New Task Created'
            body = f'Task {task.id} has been created'
            msg.attach(MIMEText(body, 'plain'))
            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.starttls()
            server.login(self.from_email, self.password)
            text = msg.as_string()
            server.sendmail(self.from_email, task.assignee_email, text)
            server.quit()
        except Exception as e:
            logging.error(f'Error sending email: {e}')