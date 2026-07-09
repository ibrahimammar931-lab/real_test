from typing import Optional
from .email_service import EmailService

class TaskService:
    def __init__(self, email_service: EmailService):
        self.email_service = email_service
    
    def create_task(self, title: str, description: str, recipient_email: str) -> Optional[dict]:
        if not title or not description or not recipient_email:
            return None
        # Task creation logic here...
        self.email_service.send_task_created_email(recipient_email, title, description)
        return {"title": title, "description": description}