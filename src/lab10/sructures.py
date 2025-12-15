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