class NativeDictionary:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size

    def hash_fun(self, key): # в качестве key поступают строки! всегда возвращает корректный индекс слота
        if self.size == 0: # если длина хэш-таблицы == 0
            return None
        # если длина хэш-таблицы > 0
        b = key.encode("utf-8") # переводит строку в байт-строку
        sum_b = 0
        for i in range(len(b)):
            sum_b += b[i]
        return sum_b % self.size  # возвращает отстаток от деления

    def is_key(self, key):  # возвращает True если ключ имеется, иначе False
        if key in self.slots:
            return True
        return False

    def put(self, key, value):  # гарантированно записываем значение value по ключу key
        index = self.hash_fun(key)
        stop = []
        # Пока значение в слоте не равно искомому и пока не попали на просмотренный слот
        while self.slots[index] != None and (index not in stop):
            stop.append(index)
            if index + 3 < self.size:
                index += 3
            else:
                index = 3 - (self.size - 1 - index)
        if self.slots[index] != None and self.slots[index] != key:
            return None
        self.slots[index] = key
        self.values[index] = value

    def get(self, key): # возвращает value для key, или None если ключ не найден
        if self.is_key(key) is True:
            index = self.hash_fun(key)
            stop = []
        # Пока значение в слоте не равно искомому и пока не попали на просмотренный слот
            while self.slots[index] != key and (index not in stop):
                stop.append(index)
                if index + 3 < self.size:
                    index += 3
                else:
                    index = 3 - (self.size - 1 - index)
            if self.slots[index] == key:
                return self.values[index]
        return None

# ht = NativeDictionary(19)
# for i in range(30):
#     ht.put('ключ '+str(i), str(i*10))
# print(ht.slots)
# print(ht.values)
# ht.put('ключ 15', 555)
# print(ht.get('ключ 15'))