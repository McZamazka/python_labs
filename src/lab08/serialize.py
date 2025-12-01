import json
from pathlib import Path
import models
from datetime import datetime, date

# st_object = models.Student("My name", "2001-05-16", "BIVT-25-3", 4.6)
students = [models.Student("My name", "2001-05-16", "BIVT-25-3", 4.6), models.Student("Xz name", "2004-05-16", "BIVT-66-6", 1.2)]

def students_to_json(students: list, path):
    data = [s.to_dict() for s in students]
    try:
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    except:
        raise FileNotFoundError("File not found")

def students_from_json(path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except:
        raise FileNotFoundError("File not found")
    data_gpa = [i.get('gpa') for i in data]
    data_birth = [i.get('birthdate').replace("-", "/") for i in data]
    try:
        data_birth = [datetime.strptime(data_date, "%Y/%m/%d") for data_date in data_birth]
    except:
        raise ValueError("warning: birthdate format might be invalid")

    if not (0 <= all(data_gpa) <= 10):
        raise ValueError("warning: gpas must be between 1 and 10")

    for key, val in zip(data, data_birth):
        key["birthdate"] = val.strftime("%Y-%m-%d")

    with open("/Users/zamazka/Documents/GitHub/python_labs/src/data/samples/lab08/students_output.json", 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


students_to_json(students, Path("/Users/zamazka/Documents/GitHub/python_labs/src/data/samples/lab08/students_input.json"))
print(students_from_json("/Users/zamazka/Documents/GitHub/python_labs/src/data/samples/lab08/students_input.json"))