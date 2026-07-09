from fastapi import FastAPI
from routes.tasks import router as task_router
import json

app = FastAPI()

app.include_router(task_router)

try:
    with open('students.json') as f:
        students_data = json.load(f)
        if 'students' not in students_data:
            raise ValueError('Invalid data format')
        students = students_data['students']
except FileNotFoundError:
    print('The students.json file was not found')
except json.JSONDecodeError:
    print('Failed to parse the students.json file')
except ValueError as e:
    print(f'Invalid data format: {e}')
else:
    print('Student data loaded successfully')