# наследуйте этот класс от HashTable
# или расширьте его методами из HashTable

class PowerSet:

    def __init__(self):  # ваша реализация хранилища
        self.slots = [] # список для внутреннего хранения

    def size(self): # количество элементов в множестве
        return len(self.slots)
    
    def get(self, value): # возвращает True если value имеется в множестве, иначе False
        if value in self.slots:
            return True
        return False

    def put(self, value): # всегда срабатывает. Добавление элемента в список, если его там нет
        if self.get(value) == False:
            self.slots.append(value)
    
    def remove(self, value): # удаление элемента из множества. Dозвращает True если value удалено иначе False
        if self.get(value) == True:
            self.slots.remove(value)
            return True
        return False

    def intersection(self, set2): # пересечение текущего множества и set2
        set_rez = PowerSet()
        for i in set2.slots:
            if self.get(i) is True:
                set_rez.put(i)
        return set_rez

    def union(self, set2): # объединение текущего множества и set2
        set_rez = PowerSet()
        # set_rez.slots = self.slots
        for i in self.slots:
            set_rez.put(i)
        for i in set2.slots:
            if self.get(i) is False:
                set_rez.put(i)
        return set_rez

    def difference(self, set2): # разница текущего множества и set2
        set_rez = PowerSet()
        for i in self.slots:
            if set2.get(i) is False:
                set_rez.put(i)
        return set_rez

    def issubset(self, set2): # возвращает True, если set2 есть подмножество текущего множества, иначе False
        for i in set2.slots:
            if self.get(i) is False:
                return False
        return True

    def get_set(self): # преобразыет список в множество
        if self.size() != 0:
            return set(self.slots)
        return {}

# ps = PowerSet()
# set2 = PowerSet()
# # print(type(ps))
# for i in range(20):
#     ps.put(str(i))
# print(ps.union(set2).get_set())
# print(ps.size())