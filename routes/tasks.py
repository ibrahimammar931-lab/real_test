from flask import Blueprint, jsonify
from services.task_service import TaskService

tasks_blueprint = Blueprint('tasks', __name__)

tasks = {
    'task1': {'status': 'completed'},
    'task2': {'status': 'pending'},
    'task3': {'status': 'completed'}
}

task_service = TaskService(tasks)

tasks_blueprint.route('/tasks/statistics', methods=['GET'])(
    lambda: jsonify(task_service.get_task_statistics())
)