from typing import Dict

class TaskStatisticsService:
    def __init__(self, tasks: Dict):
        self.tasks = tasks
    
    def total_tasks(self) -> int:
        return len(self.tasks)
    
    def completed_tasks(self) -> int:
        return sum(1 for task in self.tasks.values() if task['status'] == 'completed')
    
    def pending_tasks(self) -> int:
        return sum(1 for task in self.tasks.values() if task['status'] == 'pending')