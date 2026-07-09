from fastapi import FastAPI
from routes.tasks import router as task_router
import json

app = FastAPI()

app.include_router(task_router)

try:
    with open('students.json') as f:
        students_data = json.load(f)
except FileNotFoundError:
    print("The students.json file was not found.")
    students_data = []
except json.JSONDecodeError:
    print("Error parsing the students.json file.")
    students_data = []

def get_students():
    return students_data