from services.task_service import TaskService
from flask import Blueprint, request, jsonify

tasks = Blueprint('tasks', __name__)

task_service = TaskService()

tasks.route('/tasks', methods=['POST'])(lambda: task_service.create_task(request.json))