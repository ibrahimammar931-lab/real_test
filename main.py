import os
from email_service import EmailService

task_title = 'New Task'
task_description = 'This is a new task'
recipient_email = 'recipient-email@gmail.com'
email_password = os.environ.get('EMAIL_PASSWORD')

email_service = EmailService(email_password)
email_service.send_task_created_email(task_title, task_description, recipient_email)