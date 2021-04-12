# Модуль 5. 5. Очереди (смоделировано стандартным списком Python)

# 6.1. В классе Queue три метода: size() (количество элементов в очереди), 
# enqueue(item) -- добавить элемент в хвост очереди, 
# и dequeue(), которая возвращает элемент из головы очереди, удаляя его.

class Queue:
    def __init__(self): # инициализация хранилища данных
        self.queue = []

    def enqueue(self, item):  # вставка в хвост
        self.queue.append(item)

    def dequeue(self): # выдача из головы
        if self.queue == []:
            return None # если очередь пустая, вернуть None
        return self.queue.pop(0) # вернуть с удалением первый эл-т

    def size(self):
        return len(self.queue) # размер очереди

#  6.2. Оцените меру сложности для операций enqueue() и dequeue():
#  O(1), т.к. не зависит от кол-ва элементов в очереди

#  6.3 Функция, которая "вращает" очередь по кругу на N элементов
def round(qu:Queue(), n:int):
    while n != 0:
        qu.enqueue(qu.dequeue())
        n -= 1
        
# qu = queue_by_stack()
# qu = Queue()
# qu.enqueue(1)
# qu.enqueue(2)
# qu.enqueue(3)
# round(qu, 2)
# while qu.size() > 0:
#     print(qu.dequeue())