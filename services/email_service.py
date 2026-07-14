from email.message import EmailMessage
import smtplib

class EmailService:
    def __init__(self, smtp_server, smtp_port, sender_email, sender_password):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.sender_email = sender_email
        self.sender_password = sender_password
    
    def send_task_created_email(self, task_title, task_description, recipient_email):
        msg = EmailMessage()
        msg.set_content(f"Task '{task_title}' created: {task_description}")
        msg['subject'] = f"New Task: {task_title}" 
        msg['from'] = self.sender_email
        msg['to'] = recipient_email
        
        with smtplib.SMTP_SSL(self.smtp_server, self.smtp_port) as smtp:
            smtp.login(self.sender_email, self.sender_password)
            smtp.send_message(msg)
