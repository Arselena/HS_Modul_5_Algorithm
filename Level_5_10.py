# наследуйте этот класс от HashTable
# или расширьте его методами из HashTable

class PowerSet():

    def __init__(self):  # ваша реализация хранилища
        self.values = []

    def size(self): # количество элементов в множестве
        return len(self.values)
    
    def get(self, value): # возвращает True если value имеется в множестве, иначе False
        if value in self.values:
            return True
        return False

    def put(self, value): # всегда срабатывает. Добавление элемента в список, если его там нет
        if self.get(value) == False:
            self.values.append(value)
    
    def remove(self, value): # удаление элемента из множества. Dозвращает True если value удалено иначе False
        if self.get(value) == True:
            self.values.remove(value)
            return True
        return False

    def intersection(self, set2): # пересечение текущего множества и set2
        set_rez = []
        for i in range(len(set2)):
            if self.get(set2[i]) is True:
                set_rez.append(set2[i])
        if set_rez != []:
            return set_rez
        return None

    def union(self, set2): # объединение текущего множества и set2
        set_rez = self.values
        for i in range(len(set2)):
            if self.get(set2[i]) is False:
                set_rez.append(set2[i])
        return set_rez

    def difference(self, set2): # разница текущего множества и set2
        set_rez = []
        for i in range(len(set2)):
            if self.get(set2[i]) is False:
                set_rez.append(set2[i])
        if set_rez != []:
            return set_rez
        return None

    def issubset(self, set2): # возвращает True, если set2 есть подмножество текущего множества, иначе False
        for i in range(len(set2)):
            if self.get(set2[i]) is False:
                return False
        return True