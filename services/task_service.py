from services.email_service import EmailService

class TaskService:
    def __init__(self, email_service):
        self.email_service = email_service

    def create_task(self, task_name, to_email):
        if not task_name or not to_email:
            raise ValueError('Task name and to_email are required')
        # Create task logic here
        self.email_service.send_task_created_email(to_email, task_name)