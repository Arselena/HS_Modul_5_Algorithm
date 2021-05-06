# наследуйте этот класс от HashTable
# или расширьте его методами из HashTable

class PowerSet:

    def __init__(self):  # ваша реализация хранилища
        self.values_list = [] # список для внутреннего хранения

    def size(self): # количество элементов в множестве
        return len(self.values_list)
    
    def get(self, value): # возвращает True если value имеется в множестве, иначе False
        if value in self.values_list:
            return True
        return False

    def put(self, value): # всегда срабатывает. Добавление элемента в список, если его там нет
        if self.get(value) == False:
            self.values_list.append(value)
    
    def remove(self, value): # удаление элемента из множества. Dозвращает True если value удалено иначе False
        if self.get(value) == True:
            self.values_list.remove(value)
            return True
        return False

    def intersection(self, set2): # пересечение текущего множества и set2
        set2 = list(set2)
        set_rez = []
        for i in range(len(set2)):
            if self.get(set2[i]) is True:
                set_rez.append(set2[i])
        if set_rez != []:
            return set(set_rez)
        return None

    def union(self, set2): # объединение текущего множества и set2
        values = self.values_list
        set2 = list(set2)
        for i in range(len(set2)):
            if self.get(set2[i]) is False:
                values.append(set2[i])
        return set(values)

    def difference(self, set2): # разница текущего множества и set2
        set_rez = []
        set2 = list(set2)
        for i in range(len(set2)):
            if self.get(set2[i]) is False:
                set_rez.append(set2[i])
        if set_rez != []:
            return set(set_rez)
        return None

    def issubset(self, set2): # возвращает True, если set2 есть подмножество текущего множества, иначе False
        set2 = list(set2)
        for i in range(len(set2)):
            if self.get(set2[i]) is False:
                return False
        return True

    def get_set(self): # преобразыет список в множество
        return set(self.values_list)

# ps = PowerSet()
# for i in range(20):
#     ps.put('test' + str(i))
# print(ps.get_set())