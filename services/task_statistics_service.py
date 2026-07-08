from repositories.task_repository import TaskRepository

class TaskStatisticsService:
    def __init__(self):
        self.task_repository = TaskRepository()

    def get_total_tasks(self):
        return self.task_repository.get_total_tasks()

    def get_completed_tasks(self):
        return self.task_repository.get_completed_tasks()

    def get_pending_tasks(self):
        return self.task_repository.get_pending_tasks()