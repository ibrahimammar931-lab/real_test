import json

def load_students():
    try:
        with open('students.json') as f:
            data = json.load(f)
            if 'students' in data:
                return data['students']
            else:
                raise ValueError('Invalid JSON structure')
    except FileNotFoundError:
        print('The students.json file was not found.')
        return []
    except json.JSONDecodeError:
        print('The students.json file is not in the correct format.')
        return []
    except Exception as e:
        print(f'An error occurred: {e}')
        return []