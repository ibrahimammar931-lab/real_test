import json

def load_students():
    try:
        with open('students.json') as f:
            data = json.load(f)
            return data['students']
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []