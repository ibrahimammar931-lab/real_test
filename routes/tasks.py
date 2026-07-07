from fastapi import APIRouter, Depends
from services.task_statistics_service import TaskStatisticsService
from typing import List, Dict

router = APIRouter()

tasks = [
    {'id': 1, 'status': 'completed'},
    {'id': 2, 'status': 'pending'},
    {'id': 3, 'status': 'completed'}
]

task_statistics_service = TaskStatisticsService(tasks)

@router.get('/tasks/statistics')
def get_task_statistics():
    return task_statistics_service.get_task_statistics()