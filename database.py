import json

def load_students():
    try:
        with open('students.json') as f:
            data = json.load(f)
        return data['students']
    except FileNotFoundError:
        print('The students.json file was not found.')
        return []
    except json.JSONDecodeError:
        print('The students.json file is not a valid JSON.')
        return []