class TaskRepository:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def get_total_tasks(self):
        return len(self.tasks)

    def get_completed_tasks(self):
        return len([task for task in self.tasks if task['status'] == 'completed'])

    def get_pending_tasks(self):
        return len([task for task in self.tasks if task['status'] == 'pending'])

    def get_tasks(self):
        if not self.tasks:
            return []
        return self.tasks