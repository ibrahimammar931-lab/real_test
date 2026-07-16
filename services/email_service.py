from typing import Dict

class EmailService:
    def __init__(self, smtp_server: str, smtp_port: int, from_email: str, password: str):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.from_email = from_email
        self.password = password

    def send_task_created_email(self, task: Dict):
        # Implement email sending logic here
        # For demonstration purposes, a simple print statement is used
        print(f"Email sent for task {task['id']} with title {task['title']}")