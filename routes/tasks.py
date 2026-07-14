from flask import Blueprint, request
from .services.task_service import TaskService
from .services.email_service import EmailService

routes = Blueprint('tasks', __name__)

task_service = TaskService(EmailService('smtp.example.com', 465, 'sender@example.com', 'password'))

@routes.route('/tasks', methods=['POST'])
def create_task():
    task_title = request.json['title']
    task_description = request.json['description']
    recipient_email = request.json['recipient_email']
    task_service.create_task(task_title, task_description, recipient_email)
    return 'Task created successfully', 201
