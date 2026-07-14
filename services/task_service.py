from .email_service import EmailService

class TaskService:
    def __init__(self, email_service):
        self.email_service = email_service
    
    def create_task(self, task_title, task_description, recipient_email):
        # Task creation logic here...
        self.email_service.send_task_created_email(task_title, task_description, recipient_email)
