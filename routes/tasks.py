from services.task_service import TaskService
from services.email_service import EmailService

email_service = EmailService('smtp.example.com', 465, 'from@example.com', 'password')
task_service = TaskService(email_service)

@app.route('/tasks', methods=['POST'])
def create_task():
    task_name = request.json['task_name']
    to_email = request.json['to_email']
    task_service.create_task(task_name, to_email)
    return 'Task created successfully.'