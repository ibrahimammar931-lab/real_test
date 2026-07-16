from services.task_service import TaskService
from services.email_service import EmailService

email_service = EmailService('smtp_server', 587, 'from_email', 'password')
task_service = TaskService(email_service)

def create_task(task_name, to_email):
    task_service.create_task(task_name, to_email)