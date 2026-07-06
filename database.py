import sqlite3
from sqlite3 import Error

class TaskStatisticsService:
    def __init__(self, db_file):
        self.conn = None
        try:
            self.conn = sqlite3.connect(db_file)
        except Error as e:
            print(e)
    def get_total_tasks(self):
        try:
            cur = self.conn.cursor()
            cur.execute("SELECT COUNT(*) FROM tasks")
            return cur.fetchone()[0]
        except Error as e:
            print(e)
            return None
    def get_completed_tasks(self):
        try:
            cur = self.conn.cursor()
            cur.execute("SELECT COUNT(*) FROM tasks WHERE status = 'completed'")
            return cur.fetchone()[0]
        except Error as e:
            print(e)
            return None
    def get_pending_tasks(self):
        try:
            cur = self.conn.cursor()
            cur.execute("SELECT COUNT(*) FROM tasks WHERE status = 'pending'")
            return cur.fetchone()[0]
        except Error as e:
            print(e)
            return None