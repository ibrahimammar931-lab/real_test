from fastapi import APIRouter
from services.task_service import get_tasks, create_task

router = APIRouter()

@router.get("/tasks")
def list_tasks():
    return get_tasks()

@router.post("/tasks")
def create_new_task(title: str):
    return create_task(title)