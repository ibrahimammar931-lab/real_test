import json

def load_students():
    try:
        with open('students.json') as f:
            students = json.load(f)
        return students['students']
    except FileNotFoundError:
        print('students.json file not found')
        return []
    except json.JSONDecodeError:
        print('Error parsing students.json file')
        return []