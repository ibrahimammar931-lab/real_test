import json

def load_students():
    with open('students.json') as f:
        students = json.load(f)
    return students