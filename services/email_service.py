import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import logging

class EmailService:
    def __init__(self, smtp_server, smtp_port, from_email, password):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.from_email = from_email
        self.password = password

    def send_task_created_email(self, to_email, task_name):
        try:
            msg = MIMEMultipart()
            msg['From'] = self.from_email
            msg['To'] = to_email
            msg['Subject'] = 'New Task Created'
            body = f'A new task {task_name} has been created.'
            msg.attach(MIMEText(body, 'plain'))
            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.starttls()
            server.login(self.from_email, self.password)
            text = msg.as_string()
            server.sendmail(self.from_email, to_email, text)
            server.quit()
        except Exception as e:
            logging.error(f'Error sending email: {e}')