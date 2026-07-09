from email.message import EmailMessage
from email.utils import formatdate
import smtplib
from typing import Optional

class EmailService:
    def __init__(self, smtp_server: str, smtp_port: int, sender_email: str, sender_password: str):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.sender_email = sender_email
        self.sender_password = sender_password
    
    def send_task_created_email(self, recipient_email: str, task_title: str, task_description: str) -> None:
        try:
            msg = EmailMessage()
            msg.set_content(f"Task Title: {task_title}\nTask Description: {task_description}")
            msg['subject'] = 'New Task Created'
            msg['from'] = self.sender_email
            msg['to'] = recipient_email
            msg['date'] = formatdate(localtime = True)
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as smtp:
                smtp.starttls()
                smtp.login(self.sender_email, self.sender_password)
                smtp.send_message(msg)
        except Exception as e:
            print(f"Error sending email: {e}")