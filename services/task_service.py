from typing import Dict
from services.email_service import EmailService

class TaskService:
    def __init__(self, email_service: EmailService):
        self.email_service = email_service
    
def create_task(self, task_name: str, task_description: str, recipient_email: str):
        # Task creation logic here...
        task_id = 1  # Replace with actual task ID
        self.email_service.send_task_created_email(task_id, task_name, recipient_email)
        return {'task_id': task_id, 'task_name': task_name}