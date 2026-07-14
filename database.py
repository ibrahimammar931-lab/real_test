import json

def load_students():
    try:
        with open('students.json') as f:
            return json.load(f)
    except FileNotFoundError:
        return None