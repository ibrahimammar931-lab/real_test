from email.message import EmailMessage
import smtplib

class EmailService:
    def __init__(self, smtp_server, smtp_port, from_email, password):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.from_email = from_email
        self.password = password
    
    def send_task_created_email(self, to_email, task_name):
        msg = EmailMessage()
        msg.set_content(f'Task {task_name} has been created.')
        msg['subject'] = 'New Task Created'
        msg['to'] = to_email
        msg['from'] = self.from_email
        
        with smtplib.SMTP_SSL(self.smtp_server, self.smtp_port) as smtp:
            smtp.login(self.from_email, self.password)
            smtp.send_message(msg)