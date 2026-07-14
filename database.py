import json

def load_students():
    with open('students.json') as f:
        data = json.load(f)
    return data['students']