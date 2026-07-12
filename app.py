from fastapi import FastAPI
from routes.tasks import router as task_router
from database import load_students

app = FastAPI()

students = load_students()

app.include_router(task_router)