from email.message import EmailMessage
import smtplib

class EmailService:
    def __init__(self, mail_server, mail_port, from_addr, password):
        self.mail_server = mail_server
        self.mail_port = mail_port
        self.from_addr = from_addr
        self.password = password
    
    def send_task_created_email(self, to_addr, task_details):
        msg = EmailMessage()
        msg.set_content(f'Task created: {task_details}')
        msg['subject'] = 'New Task Created'
        msg['from'] = self.from_addr
        msg['to'] = to_addr
        
        with smtplib.SMTP_SSL(self.mail_server, self.mail_port) as smtp:
            smtp.login(self.from_addr, self.password)
            smtp.send_message(msg)
