from fastapi import APIRouter, Depends
from services.task_statistics_service import TaskStatisticsService
from repositories.task_repository import TaskRepository

router = APIRouter()

task_repository = TaskRepository()
task_statistics_service = TaskStatisticsService(task_repository)

@router.get('/tasks/statistics')
def get_task_statistics():
    return task_statistics_service.get_task_statistics()