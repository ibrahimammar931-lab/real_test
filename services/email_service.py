from email.message import EmailMessage
import smtplib
from typing import Dict

class EmailService:
    def __init__(self, sender_email: str, sender_password: str, smtp_server: str, smtp_port: int):
        self.sender_email = sender_email
        self.sender_password = sender_password
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
    
def send_task_created_email(self, task_id: int, task_name: str, recipient_email: str):
        msg = EmailMessage()
        msg.set_content(f'Task {task_id}: {task_name} has been created.')
        msg['subject'] = f'Task Created: {task_name}'
        msg['to'] = recipient_email
        msg['from'] = self.sender_email
        with smtplib.SMTP_SSL(self.smtp_server, self.smtp_port) as smtp:
            smtp.login(self.sender_email, self.sender_password)
            smtp.send_message(msg)
        print('Email sent successfully.')