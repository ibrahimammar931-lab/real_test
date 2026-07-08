from services.task_statistics_service import TaskStatisticsService
from flask import Blueprint, jsonify

routes = Blueprint('tasks', __name__)

task_statistics_service = TaskStatisticsService()

@routes.route('/tasks/statistics', methods=['GET'])
def get_task_statistics():
    total_tasks = task_statistics_service.get_total_tasks()
    completed_tasks = task_statistics_service.get_completed_tasks()
    pending_tasks = task_statistics_service.get_pending_tasks()
    return jsonify({'total_tasks': total_tasks, 'completed_tasks': completed_tasks, 'pending_tasks': pending_tasks})