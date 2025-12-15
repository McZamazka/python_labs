<h1>Прграммирование и алгоритмизация (Лабораторные)</h1>

<h2>Лабораторная №9:</h2>

```python
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
```
![exe1_1_1!](/images/lab09/exe1_1.png)
![exe1_1_1!](/images/lab09/exe1_2.png)

<h2>Лабораторная №10:</h2>

**Задание №1:**

```python
from collections import deque

class Stack:
    def __init__(self, array: list = []):
        # внутреннее хранилище стека
        self._data = array

    def push(self, item):
        # корректно: добавление в конец списка O(1) амортизированно
        self._data.append(item)

    def pop(self):
        # TODO: добавить обработку случая пустого стека (сейчас IndexError от list)
        try:
            return self._data.pop()
        except IndexError:
            raise IndexError('Stack is empty')

    def peek(self):
        try:
            return self._data[-1]
        except IndexError:
            return None

    def is_empty(self) -> bool:
        # TODO: улучшить реализацию
        if len(self._data) == 0:
            return True
        else:
            return False

    def __len__(self):
        return len(self._data)

class Queue:
    def __init__(self, array: list = []):
        # ошибка: вместо deque используется list → операции O(n)
        self._data = deque(array)

    def enqueue(self, item):
        # ошибка: вставка в начало, а не в конец
        self._data.append(item)

    def dequeue(self):
        # ошибка: удаление с конца, а не с начала
        return self._data.popleft()

    def peek(self):
        # TODO: корректное поведение при пустой очереди
        if len(self._data) == 0:
            raise IndexError('Queue is empty')
        return self._data[0]

    def is_empty(self) -> bool:
        return not self._data

    def __len__(self):
        return len(self._data)

if __name__ == '__main__':
    s = Stack([])
    s.push(2)
    s.push(12)
    s.push(52)
    print(f"Пуст ли стек: {s.is_empty()}")
    print(f"Верхний элемент: {s.peek()}")
    print(f"Длина стека: {len(s)}")

    print("--------------------------------------")
    q = Queue()
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)
    print(f"Элемент из начала: {q.dequeue()}")
    print(f"Певрый элемент: {q.peek()}")
    print(f"Длина: {len(q)}")
 ```
**Задание №2:**

```python
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return str(self.value)


class SinglyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self._size = 0

    def append(self, value):
        """Добавить элемент в конец списка"""
        new_node = Node(value)

        if self.head is None:  # Если список пустой
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node  # Старый tail указывает на новый узел
            self.tail = new_node  # Обновляем tail на новый узел

        self._size += 1

    def prepend(self, value):
        """Добавить элемент в начало списка"""
        new_node = Node(value, next=self.head)
        new_node.next = self.head
        self.head = new_node
        self._size += 1
        # TODO: обновить размер

    def insert(self, idx, value):
        if idx < 0:
            raise IndexError("negative index is not supported")

        new_node = Node(value)

        if idx == 0:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head

        for _ in range(idx - 1):
            if current is None:
                raise IndexError("list index out of range")
            current = current.next

        if current is None:
            raise IndexError("list index out of range")
        new_node.next = current.next
        current.next = new_node
        self._size += 1

    def remove_at(self, idx):
        if idx < 0:
            raise IndexError("negative index is not supported")

        if self.head is None or idx >= self._size:
            raise IndexError("list index out of range")

        if idx == 0:
            value = self.head.value
            self.head = self.head.next

            if self.head is None:
                self.tail = None

            self._size -= 1
            return value

        current = self.head
        for _ in range(idx - 1):
            current = current.next

        node_to_delete = current.next
        value = node_to_delete.value

        current.next = node_to_delete.next

        if node_to_delete == self.tail:
            self.tail = current

        self._size -= 1
        return value

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current.value
            current = current.next

    def __len__(self):
        return self._size

    def __repr__(self):
        values = list(self)
        return f"SinglyLinkedList({values})"


linkedlist = SinglyLinkedList()
linkedlist.append(1)
linkedlist.append(2)
linkedlist.append(3)
linkedlist.append(4)
print(f"1. Добавление в конец: {linkedlist}")
linkedlist.prepend(5)
print(f"2. Добавление в начало (5): {linkedlist}")
linkedlist.insert(2, 15)
print(f"3. Вставка 15 по индексу 2: {linkedlist}")
linkedlist.remove_at(2)
print(f"4. Удаление 15 (середина): {linkedlist}")
print(f"5. Размер: {len(linkedlist)}")
print(f"6. Пуст ли список? {len(linkedlist) == 0}")
```

![exe1_1_1!](/images/lab10/exe1_1.png)
![exe1_1_1!](/images/lab10/exe2_1.png)