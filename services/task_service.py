from services.email_service import EmailService

class TaskService:
    def __init__(self, email_service):
        self.email_service = email_service
    
    def create_task(self, task):
        # Task creation logic
        self.email_service.send_task_created_email(task)
        return task