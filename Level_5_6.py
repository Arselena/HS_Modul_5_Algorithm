# Модуль 5. 6. Двусторонняя очередь (deque)
# 7.1. Почему и как будет различаться мера сложности для addHead/removeHead и addTail/removeTail?


class Deque:
    def __init__(self):  # инициализация внутреннего хранилища
        self.deque = []

    def addFront(self, item):  # добавление в голову
        self.deque.insert(0, item)

    def addTail(self, item):  # добавление в хвост
        self.deque.append(item)

    def removeFront(self):  # удаление из головы
        if self.deque == []:
            return None # если очередь пустая, вернуть None
        return self.deque.pop(0) # вернуть с удалением первый эл-т

    def removeTail(self):  # удаление из хвоста
        if self.deque == []:
            return None # если очередь пустая, вернуть None
        return self.deque.pop() # вернуть с удалением последний эл-т

    def size(self):
        return len(self.deque) # размер очереди

    def print_all(self):
        for i in range(self.size()):
            print(self.deque[i])

# 7.1. Почему и как будет различаться мера сложности для addHead/removeHead и addTail/removeTail?
# Для addHead/removeHead мера сложности будет O(n), т.к. надо заного индексировать все эл-ы списка
# Для addTail/removeTail мера сложность O(1)

# 7.2. Напишите функцию, которая с помощью deque проверяет, является ли некоторая строка палиндромом
def polinom(s):
    qu1 = Deque()
    qu2 = Deque()
    for i in range(len(s)):
        qu1.addTail(s[i])
        qu2.addFront(s[i])
    if qu1.deque == qu2.deque:
        return True
    return False


# deq = Deque()
# deq.addFront("f1")
# deq.addTail("t1")
# deq.addFront("f2")
# deq.addTail("t2")
# while deq.size() > 0:
#     print(deq.removeFront())
#     print(deq.removeTail())

# print(polinom('11211'))
