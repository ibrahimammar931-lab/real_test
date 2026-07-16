from email_service import EmailService

class TaskService:
    def __init__(self):
        self.email_service = EmailService()
    
    def create_task(self, task):
        # Create task logic here...
        self.email_service.send_task_created_email(task)
        return task