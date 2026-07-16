from email.message import EmailMessage
from email.utils import formatdate
import smtplib

class EmailService:
    def __init__(self, smtp_server, smtp_port, from_email, password):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.from_email = from_email
        self.password = password
    
    def send_task_created_email(self, task):
        msg = EmailMessage()
        msg['Subject'] = 'New Task Created'
        msg['From'] = self.from_email
        msg['To'] = 'recipient@example.com'
        msg['Date'] = formatdate(localtime = True)
        msg.set_content(f'Task {task.id} created: {task.name}')
        
        with smtplib.SMTP_SSL(self.smtp_server, self.smtp_port) as smtp:
            smtp.login(self.from_email, self.password)
            smtp.send_message(msg)