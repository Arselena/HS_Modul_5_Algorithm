# 12. Кэш

class NativeCache:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size  # массив ключей
        self.values = [None] * self.size  # массив значений
        self.hits = [0] * self.size  # массив кол-ва обращений

    def hash_fun(self, key): # в качестве key поступают строки! всегда возвращает корректный индекс слота
        if self.size == 0: # если длина хэш-таблицы == 0
            return None
        # если длина хэш-таблицы > 0
        index = 0
        for c in key:
            code = ord(c)  # Функция ord() для символа x вернет число, из таблицы символов Unicode представляющее его позицию.
            index = (index * 17 + code) % self.size
        return index  # возвращает остаток от деления

    def is_key(self, key):  # возвращает True если ключ имеется, иначе False
        if key in self.slots:
            return True
        return False

    def min_index(self):
        min = self.hits[0]
        index = 0
        for i in range(1, self.size):
            if self.hits[i] < min:
                min = self.hits[i]
                index = i
        return index

    def find_index(self, key, None_or_key): # None_or_key - для поиска либо пустого слота(None), лобо слота со значением key
        index = self.hash_fun(key)
        stop = [] # массив просмотренных слотов
        # Пока значение в слоте не равно искомому и пока не попали на просмотренный слот
        while self.slots[index] != None_or_key and (index not in stop):
            stop.append(index)
            if index + 3 < self.size:
                index += 3
            else:
                index = 3 - (self.size - index)
        return index

    def put(self, key, value):  # гарантированно записываем значение value по ключу key
        if self.is_key(key) is True: # если ключ есть, то меняем соответствующее ему значение
            self.values[self.find_index(key, key)] = value
            # self.hits[index] = 0  # наверное не обнуляем кол-во обращений
            return
        index = self.find_index(key, None)
        if self.slots[index] != None:  # если все слоты заняты, то присваиваем индексу значение с минимальным обращением
            index = self.min_index()
            self.hits[index] = 0 # обнуляем кол-во обращений
            
        self.slots[index] = key
        self.values[index] = value

    def get(self, key): # возвращает value для key, или None если ключ не найден
        if self.is_key(key) is True:
            index = self.find_index(key, key)
            self.hits[index] += 1
            return self.values[index]
        return None

# ht = NativeCache(17)
# for i in range(17):
#     ht.put('ключ '+str(i), str(i*10))
#     ht.get('ключ '+str(i))
# print(ht.hits)
# for i in range(16, 34):
#     ht.put('ключ '+str(i), str(i*10))
#     ht.get('ключ '+str(i))
#     ht.get('ключ '+str(i))

# ht.put('ключ 25', '555')
# print(ht.slots)
# print(ht.values)
# print(ht.get('ключ 25'))