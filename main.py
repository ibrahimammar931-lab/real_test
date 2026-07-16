from email_service import EmailService
from task_service import TaskService

def main():
    sender_email = 'your-email@gmail.com'
    sender_password = 'your-password'
    receiver_email = 'receiver-email@gmail.com'
    email_service = EmailService(sender_email, sender_password, receiver_email)
    task_service = TaskService(email_service)
    task_service.create_task('New Task', 'This is a new task')