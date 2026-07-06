from .task_statistics_service import TaskStatisticsService

class TaskService:
    def __init__(self, tasks: Dict):
        self.tasks = tasks
        self.task_statistics_service = TaskStatisticsService(tasks)
    
    def get_task_statistics(self):
        return {
            'total': self.task_statistics_service.total_tasks(),
            'completed': self.task_statistics_service.completed_tasks(),
            'pending': self.task_statistics_service.pending_tasks()
        }