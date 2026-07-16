from services.task_service import TaskService
from services.email_service import EmailService

class Task:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class TasksRoute:
    def __init__(self, task_service):
        self.task_service = task_service
    
    def create_task(self, task):
        return self.task_service.create_task(task)

task_service = TaskService(EmailService('smtp.example.com', 465, 'sender@example.com', 'password'))
tasks_route = TasksRoute(task_service)