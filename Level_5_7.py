# 7. Упорядоченный список

class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

# 7.1. Дополнительную опцию asc в конструкторе OrderedList, которая указывает, по возрастанию (True) или по убыванию (False) должны храниться элементы в массиве.
# Эту опцию сделайте приватной -- изменять её можно только в конструкторе и методе очистки clean().
class OrderedList:
    def __init__(self, asc = True):
        self.head = None
        self.tail = None
        self.__ascending = asc

# 7.2. Метод сравнения двух значений compare(). Пока сделайте базовый вариант этого метода, который сравнивает числовые значения.
    def compare(self, v1, v2):
        if v1 < v2:
            return -1
        elif v1 > v2:
            return 1
        return 0
        # -1 если v1 < v2
        # 0 если v1 == v2
        # +1 если v1 > v2

# 7.3. Добавление нового элемента по значению add() с единственным параметром -- новым добавляемым значением (новый узел для него создавайте внутри метода add). 
# Элемент должен вставиться автоматически между элементами с двумя подходящими значениями (либо в начало или конец списка) с учётом его значения и признака упорядоченности. 
# Используйте для этого метод сравнения значений из предыдущего пункта.
    def add(self, value):
        new_node = Node(value)

        if self.head is None: # если список пустой
            self.head = new_node
            self.tail = new_node
            return

        node = self.head  # задаем начало поиска узла с головы

        # в переменную flag запишем значение для сравнения двух чисел. И будем использовать один цикл для сортировки по возрастанию и убыванию
        flag = -1  # значение для сортировки по возрастанию
        if self.__ascending == False:  
            flag = 1  # значение для сортировки по убыванию
        
        while (self.compare(node.value, new_node.value) == flag) or (self.compare(node.value, new_node.value) == 0): # опредеяем место вставки узла
            node = node.next 
            if node is None:
                break
                
        if node == None: # вставка в конец списка
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

        elif node == self.head: # вставка в начало списка
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
            
        else: # вставка в середину
            node.prev.next = new_node
            new_node.prev = node.prev
            new_node.next = node
            node.prev = new_node
        
        pass

# 7.5. Переделайте функцию поиска элемента по значению с учётом признака упорядоченности и возможности раннего прерывания поиска, 
# если найден заведомо больший или меньший элемент, нежели искомый. Оцените сложность операции поиска, изменилась ли она ?

# Сложность алгоритма зависит от искомого значения и сортировки. Эффективность будет меньше n, т.е. o(n)  
# Можно сделать сложность O(log n) через бинарный поиск. Проверим средний элемент, если он больше искомого, то отбросим вторую половину массива — там его точно нет. 
# Если же меньше, то наоборот — отбросим начальную половину. И так будем продолжать делить пополам, в итоге проверим log n элементов.
    def find(self, val):
        if self.head == None:  # если список пустой, то вернуть None
            return None

        flag = -1  # значение для сортировки по возрастанию
        if self.__ascending == False:  
            flag = 1  # значение для сортировки по убыванию
        node = self.head
        while (self.compare(node.value, val) == flag) or (self.compare(node.value, val) == 0):
            if self.compare(node.value, val) == 0:
                return node 
            node = node.next
            if node == None:
                break
        return None # здесь будет ваш код

    def delete(self, val, all=False): # удаление элемента по его значению (остаётся без изменений, как в классе LinkedList2)
                                      # метод дополнен удалением всех узлов по конкретному значению (флажок all=True).
        if self.head == None:  # если список пустой, то выйти
            return
        node = self.head
        while node:
            if node.value == val:
                if node == self.head == self.tail:
                    self.clean()
                    return
                if node == self.head:  # если удаляется "голова", то переопределяем голову и пред.узел
                    self.head = node.next
                    node = self.head
                    node.prev = None
                elif node == self.tail:  # если удаляется "хвост", то переопределяем хвост
                    self.tail = node.prev
                    node.prev.next = None
                else:
                    node.prev.next = node.next
                    node.next.prev = node.prev
                if all == False:
                    return
            node = node.next
        pass 
        
    def clean(self, asc=True):
        self.__ascending = asc
        self.__init__()
        pass # здесь будет ваш код

    def len(self):
        node = self.head
        l = 0
        while node:
            l +=1
            node = node.next
        return l # здесь будет ваш код

    def get_all(self):
        r = []
        node = self.head
        while node != None:
            r.append(node)
            node = node.next
        return r

    def print_all(self):
        node = self.head
        while node:
            print(node.value)
            node = node.next

# 7.4. Создайте OrderedStringList -- наследник текущего класса, который будет упорядоченно хранить строки. 
# Для этого переопределите в нём метод сравнения значений -- он должен сравнивать строки, очищенные от начальных и конечных пробелов.
class OrderedStringList(OrderedList):
    def __init__(self, asc=True):
        super(OrderedStringList, self).__init__(asc)

    def compare(self, v1:str, v2:str):
        # переопределённая версия для строк
        if v1.strip() < v2.strip():
            return -1
        elif v1.strip() > v2.strip():
            return 1
        return 0

# s_list = OrderedList()
# s_list.add(6)
# s_list.add(2)
# s_list.add(4)
# s_list.add(1)
# print(s_list.len())
# str_list = OrderedStringList()
# str_list.add(' 2')
# str_list.add('  3 ')
# str_list.add('1 ')
# str_list.print_all()
# print(str_list.find('3').value)
# s_list.delete(5)
# str_list.print_all()
# print(s_list.find(5))
