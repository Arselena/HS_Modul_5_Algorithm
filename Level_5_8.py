# 8. Хэширование

class HashTable:
    def __init__(self, sz, stp):
        self.size = sz  # размер хэш-таблицы (например 17 или 19)
        self.step = stp # длина шага (количество слотов) для поиска следующего свободного слота (например, 3)
        self.slots = [None] * self.size  # 17 раз None (по размеру хэш-таблицы)

    def hash_fun(self, value): # по входному значению вычисляет индекс слота, в качестве value поступают строки! Всегда возвращает корректный индекс слота
        if self.size == 0: # если длина хэш-таблицы == 0
            return None
        # если длина хэш-таблицы > 0
        b = value.encode("utf-8") # переводит строку в байт-строку
        sum_b = 0
        for i in range(len(b)):
            sum_b += b[i]
        print(sum_b)
        return sum_b % self.size  # возвращает отстаток от деления

    def seek_slot(self, value):  # находит индекс пустого слота для значения, или None
        if self.size == 0: # если длина хэш-таблицы == 0
            return None 
        index = self.hash_fun(value)
        stop = []  # массив для просмотренных слотов
        if self.size > 1:  # если длина хэш-таблицы > 1
            # Пока значение в слоте не пустое и пока не попали на просмотренный слот
            while (self.slots[index] is not None) and (index not in stop):
                stop.append(index) # добавляем индекс в массив просмотренных слотов
                if index + self.step < self.size: # увеличиваем индекс на шаг, если не выходим из диапазона таблицы
                    index += self.step
                else:  # если выходим из диапазона таблицы, то начинаем перебор с начала
                    index = self.step - (self.size - 1 - index)
        if self.slots[index] is None: # если слот свободен, то возвращаем индекс
            return index
        return None

    def put(self, value): # записываем значение по хэш-функции. Возвращается индекс слота или None, если из-за коллизий элемент не удаётся разместить 
        index = self.seek_slot(value) # находим свободный слот или None
        if index is not None:
            self.slots[index] = value
            return index
        return None

    def find(self, value): # находит индекс слота со значением, или None
        index = self.hash_fun(value)
        stop = []
        # Пока значение в слоте не равно искомому и пока не попали на просмотренный слот
        while self.slots[index] != value and (index not in stop):
            stop.append(index)
            if index + self.step < self.size:
                index += self.step
            else:
                index = self.step - (self.size - 1 - index)
        if self.slots[index] == value:
            return index
        return None