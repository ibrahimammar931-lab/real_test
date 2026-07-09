from fastapi import FastAPI
from routes.tasks import router as task_router
import json

app = FastAPI()

def get_students():
    with open('students.json') as f:
        return json.load(f)

students = get_students()

app.include_router(task_router)