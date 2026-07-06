from fastapi import APIRouter
from services.task_service import get_tasks

router = APIRouter()

@router.get("/tasks")
def list_tasks():
    return get_tasks()