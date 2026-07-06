from services.logging_service import LoggingService

class TaskService:
    def __init__(self):
        self.logging_service = LoggingService()
    def create_task(self, task):
        # existing task creation logic
        self.logging_service.log_task_created(task)
    def delete_task(self, task):
        # existing task deletion logic
        self.logging_service.log_task_deleted(task)