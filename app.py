from fastapi import FastAPI
from routes.tasks import router as task_router
from database import load_students

app = FastAPI()

app.include_router(task_router)

students = load_students()