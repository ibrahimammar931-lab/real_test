from fastapi import APIRouter
from services.task_statistics_service import TaskStatisticsService

router = APIRouter()

task_statistics_service = TaskStatisticsService()

@router.get('/task-statistics')
def get_task_statistics():
    task_statistics = task_statistics_service.get_task_statistics()
    return task_statistics