from fastapi import APIRouter, HTTPException
from services.task_service import TaskService
from services.email_service import EmailService

router = APIRouter()

task_service = TaskService(EmailService('sender@example.com', 'password', 'smtp.example.com', 465))

@router.post('/tasks/')
def create_task(task_name: str, task_description: str, recipient_email: str):
    try:
        task_service.create_task(task_name, task_description, recipient_email)
        return {'message': 'Task created successfully.'}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))