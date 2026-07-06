import logging

class LoggingService:
    def log_task_created(self, task):
        logging.info(f'Task {task} created')
    def log_task_deleted(self, task):
        logging.info(f'Task {task} deleted')