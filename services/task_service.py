from services.email_service import EmailService

class TaskService:
    def __init__(self):
        self.email_service = EmailService()

    def create_task(self, task):
        # existing task creation logic
        self.email_service.send_task_created_email(task)
        return task