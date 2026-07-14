import json

def load_students():
    with open('students.json') as f:
        return json.load(f)

students = load_students()