class TaskStatisticsService:
    def __init__(self, db):
        self.db = db
    
    def get_total_tasks(self):
        try:
            return self.db.execute("SELECT COUNT(*) FROM tasks").fetchone()[0]
        except Exception as e:
            print(f"Error: {e}")
            return None
    
    def get_completed_tasks(self):
        try:
            return self.db.execute("SELECT COUNT(*) FROM tasks WHERE status = 'completed'").fetchone()[0]
        except Exception as e:
            print(f"Error: {e}")
            return None
    
    def get_pending_tasks(self):
        try:
            return self.db.execute("SELECT COUNT(*) FROM tasks WHERE status = 'pending'").fetchone()[0]
        except Exception as e:
            print(f"Error: {e}")
            return None