# 8. Хэширование

class HashTable:
    def __init__(self, sz, stp):
        self.size = sz  # размер хэш-таблицы (например 17 или 19)
        self.step = stp # длина шага (количество слотов) для поиска следующего свободного слота (например, 3)
        self.slots = [None] * self.size  # 17 раз None (по размеру хэш-таблицы)

    def hash_fun(self, value): # по входному значению вычисляет индекс слота, в качестве value поступают строки!
        if self.size == 0: # если длина хэш-таблицы == 0
            return None
        if self.size == 1: # если длина хэш-таблицы == 0
            return 0
        b = value.encode("utf-8") # переводит строку в байт-строку
        sum_b = 0
        for i in range(len(b)):
            sum_b += b[i]
        # всегда возвращает корректный индекс слота
        return sum_b % self.size

    def seek_slot(self, value):
        # находит индекс пустого слота для значения, или None
        index = self.hash_fun(value)
        stop = []
        while (self.slots[index] is not None) and (index not in stop):
            stop.append(index)
            if index + self.step < self.size:
                index += self.step
            else:
                index = self.step - (self.size - index)
        return index

    def put(self, value):
        # записываем значение по хэш-функции
        # возвращается индекс слота или None,vесли из-за коллизий элемент не удаётся разместить 
        index = self.seek_slot(value)
        if index is not None:
            self.slots[index] = value
            return index
        return None

    def find(self, value): # находит индекс слота со значением, или None
        index = self.hash_fun(value)
        stop = []
        while self.slots[index] != value and (index not in stop):
            stop.append(index)
            if index + self.step < self.size:
                index += self.step
            else:
                index = self.step - (self.size - index)
        if self.slots[index] == value:
            return index
        return None

# ht = HashTable(128, 3)
# print(ht.hash_fun('3'))
# g0 = ht.put("value")
# print(g0)
# g1 = ht.put("value1")
# print(g1)
# g2 = ht.put("value11")
# print(g2)
# print(ht.find("value11"))

# ht3 = HashTable(128, 3)
# for i in range(127):
#     ht3.put(str(i))
# print(ht3.slots)
# print(ht3.find('300'))