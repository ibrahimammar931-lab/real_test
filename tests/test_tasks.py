import unittest
from unittest.mock import patch
from services.task_service import create_task
from services.email_service import EmailService

class TestTaskService(unittest.TestCase):
    @patch.object(EmailService, 'send_task_created_email')
    def test_create_task_sends_email(self, mock_send_email):
        create_task('New Task')
        mock_send_email.assert_called_once_with('New Task')

if __name__ == '__main__':
    unittest.main()