# Модуль 5. 5. Очереди (смоделировано стандартным списком Python)

# 6.1. В классе Queue три метода: size() (количество элементов в очереди), 
# enqueue(item) -- добавить элемент в хвост очереди, 
# и dequeue(), которая возвращает элемент из головы очереди, удаляя его.
import ctypes
from Level_5_4 import Stack

class Queue:
    def __init__(self): # инициализация хранилища данных
        self.queue = []

    def make_queue(self, new_capacity):
        return (new_capacity * ctypes.py_object)()
    
    def size(self):
        return len(self.queue)

    def enqueue(self, value):  # вставка в конец очереди (хвост)
        new_queue = ((self.size() + 1) * ctypes.py_object)()  # расширяем массив памяти на 1 ячейку
        size = self.size()
        for i in range(size):
            new_queue[i] = self.queue[i]
        new_queue[size] = value
        self.queue = new_queue

    def dequeue(self):
        size = self.size()
        if size == 0:
            return None # если очередь пустая
        new_queue = ((self.size() - 1) * ctypes.py_object)()
        for i in range(size - 1):
            new_queue[i] = self.queue[i+1]
        head_element = self.queue[0]
        self.queue = new_queue
        return head_element

#  6.2. Оцените меру сложности для операций enqueue() и dequeue():
#  enqueue() - O(1), т.к. не зависит от кол-ва элементов в очереди
#  dequeue() - O(n), т.к. зависит от кол-ва элементов в очереди

#  6.3 Функция, которая "вращает" очередь по кругу на N элементов
def round(qu:Queue(), n:int):
    while n != 0:
        qu.enqueue(qu.dequeue())
        n -= 1

# 6.4. Попробуйте реализовать очередь с помощью двух стеков.

class queue_by_stack():
    def __init__(self):
        self.st1 = Stack()
        self.st2 = Stack()

    def enqueue(self, item):  # вставка в хвост
        self.st1.push(item)

    def dequeue(self): # выдача из головы
        if self.st1.size() == 0:
            return None
        for i in range(self.st1.size()):
            self.st2.push(self.st1.pop()) # реверс 1-ого стека во 2-ой
        res = self.st2.pop()  # удаляем последний эл-т реверсного стека
        for i in range(self.st2.size()):
            self.st1.push(self.st2.pop()) # делаем обратный реверс
        return res

    def size(self):
        return self.st1.size() # размер очереди

# qu = queue_by_stack()
# qu = Queue()
# qu.enqueue(1)
# qu.enqueue(2)
# qu.enqueue(3)
# round(qu, 2)
# while qu.size() > 0:
#     print(qu.dequeue())
# print(qu.size())