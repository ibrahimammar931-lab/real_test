from services.email_service import EmailService

class TaskService:
    def __init__(self, email_service):
        self.email_service = email_service

    def create_task(self, task):
        # Create task logic here
        self.email_service.send_task_created_email(task)