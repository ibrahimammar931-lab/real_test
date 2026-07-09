from flask import Blueprint, request, jsonify
from .services.task_service import TaskService
from .services.email_service import EmailService

tasks_blueprint = Blueprint('tasks', __name__)

task_service = TaskService(EmailService('smtp.example.com', 587, 'sender@example.com', 'password'))

tasks_blueprint.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    task = task_service.create_task(data['title'], data['description'], data['recipient_email'])
    if task:
        return jsonify(task), 201
    return jsonify({"error": "Task creation failed"}), 400