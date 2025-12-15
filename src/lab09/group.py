import csv
from pathlib import Path
import sys

from openpyxl import writer

sys.path.append("/Users/zamazka/Documents/GitHub/python_labs/src/lab08/")
from models import Student

class Group:
    def __init__(self, storage_path: str):
        self.path = Path(storage_path)
        self.reader = None
        self.list_students = []
        if not self.path.exists():
            self.path.write_text("", encoding="utf-8")
        self._read_all()

    def _read_all(self):
        # TODO: реализовать чтение строк из csv
        try:
            with open(self.path, "r", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                self.reader = list(reader)
        except FileNotFoundError:
            raise FileNotFoundError("File not found")

    def list(self):
        self.list_students = [i.get("fio") for i in self.reader]
        return self.list_students

    def add(self, student: Student):
        student_dict = student.to_dict()
        fieldnames = student_dict.keys()
        self.reader.append(student_dict)
        try:
            with open(self.path, "a", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writerow(student_dict)
        except FileNotFoundError:
            raise FileNotFoundError("File not found")


    def find(self, substr: str):
        # TODO: реализовать метод find()
        rows = self.reader
        return [r for r in rows if substr in r["fio"]]

    def remove(self, fio: str):
        # TODO: реализовать метод remove()
        rows = self.reader
        if len(rows) != 0:
            for i, r in enumerate(rows):
                if r["fio"] == fio:
                    rows.pop(i)
                    break
        else:
            raise ValueError("File not must be empty")

        try:
            with open(self.path, "w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=rows[0].keys())
                writer.writeheader()
                for r in rows:
                    r = {key: r.get(key, "") for key in r}
                    writer.writerow(r)
        except FileNotFoundError:
            raise FileNotFoundError("File not found")
        return rows

    def update(self, fion: str, **fields):
        # TODO: реализовать метод update()
        self._read_all()
        stud_vals = fields.values()
        if fion in self.list_students:
            raise ValueError("fio already exists")
        else:
            stud = self.find(fion)[0]
            for key, val in zip(stud.keys(), stud_vals):
                stud[key] = val
        self.reader = self.remove(fion)

        self.reader.append(stud)
        try:
            with open(self.path, "w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=self.reader[0].keys())
                writer.writeheader()
                for r in self.reader:
                    r = {key: r.get(key, "") for key in r}
                    writer.writerow(r)
        except FileNotFoundError:
            raise FileNotFoundError("File not found")

data_update = {
    'fio': 'Киселева Елена',
    'birthdate': '1991-01-01',
    'group': 'BIVT25-3',
    'gpa': 2.1
}

st = Group("/Users/zamazka/Documents/GitHub/python_labs/src/data/samples/lab09/students.csv")
st1 = Student("Bbbbbb", "2007-12-20", "BIVT", 4.6)
st.add(st1)
print(st.list())
st.find("Bbbbbb")
st.update('Киселева Елена', **data_update)
