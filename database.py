import json

def load_students():
    try:
        with open('students.json') as f:
            data = json.load(f)
            return data['students']
    except FileNotFoundError:
        print("The file does not exist")
    except json.JSONDecodeError:
        print("Error parsing JSON")