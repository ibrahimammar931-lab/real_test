from typing import Dict

class TaskStatisticsService:
    def __init__(self, tasks: list):
        self.tasks = tasks
    
    def get_task_statistics(self) -> Dict:
        total_tasks = len(self.tasks)
        completed_tasks = sum(1 for task in self.tasks if task['status'] == 'completed')
        pending_tasks = sum(1 for task in self.tasks if task['status'] == 'pending')
        
        return {
            'total_tasks': total_tasks,
            'completed_tasks': completed_tasks,
            'pending_tasks': pending_tasks
        }