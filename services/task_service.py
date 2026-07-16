from typing import Dict
from services.email_service import EmailService
from models import TaskModel  # Assuming TaskModel is the actual database model

class TaskService:
    def __init__(self, email_service: EmailService):
        self.email_service = email_service

    def create_task(self, task_data: Dict) -> TaskModel:
        try:
            # Create a new task using the actual TaskModel
            task = TaskModel(**task_data)
            task.save()
            self.email_service.send_task_created_email(task.__dict__)
            return task
        except Exception as e:
            # Handle exceptions during task creation
            print(f"Error creating task: {str(e)}")
            raise