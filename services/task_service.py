from services.email_service import EmailService

def get_tasks():
    return [
        {"id": 1, "title": "Buy milk"}
    ]

def create_task(title):
    task = {"id": 2, "title": title}
    email_service = EmailService('sender@example.com', 'password', 'receiver@example.com')
    email_service.send_task_created_email(title)
    return task