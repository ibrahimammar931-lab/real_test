from repositories.task_repository import TaskRepository

class TaskStatisticsService:
    def __init__(self, task_repository: TaskRepository):
        self.task_repository = task_repository

    def get_task_statistics(self):
        tasks = self.task_repository.get_all_tasks()
        total_tasks = len(tasks)
        completed_tasks = len([task for task in tasks if task['status'] == 'completed'])
        pending_tasks = len([task for task in tasks if task['status'] == 'pending'])
        return {
            'total_tasks': total_tasks,
            'completed_tasks': completed_tasks,
            'pending_tasks': pending_tasks
        }