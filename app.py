from fastapi import FastAPI
from routes.tasks import router as task_router
import json

app = FastAPI()

with open('students.json') as f:
    students = json.load(f)

app.include_router(task_router)
