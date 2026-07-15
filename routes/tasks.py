from services.task_service import TaskService

task_service = TaskService()
@app.route('/tasks', methods=['POST'])
def create_task():
    task = request.get_json()
    task_service.create_task(task)
    return 'Task created successfully'