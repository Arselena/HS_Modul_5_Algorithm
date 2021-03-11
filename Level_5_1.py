# Модуль 5. Алгоритмы.

class Node:  # Node будут два элемента: value (само данное) и next -- "связь", по сути указатель на следующий узел. 

    def __init__(self, v):
        self.value = v
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item): # добавляет новый узел в конец списка
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def print_all_nodes(self): # метод отладочного вывода списка
        node = self.head
        while node != None:
            print(node.value)
            node = node.next

    def find(self, val):  # найти нужный узел по заданному значению
        node = self.head
        while node:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val): # 1.4. Добавьте в класс LinkedList метод поиска всех узлов по конкретному значению 
                             # (возвращается стандартный питоновский список найденных узлов).
        s = []
        node = self.head
        while node:
            if node.value == val:
                s.append(node)
            node = node.next
        return s

    def delete(self, val, all=False): # 1.1. Добавьте в класс LinkedList метод удаления одного узла по его значению
                                     # 1.2. Дополните этот метод удалением всех узлов по конкретному значению (флажок all=True).
        if self.head is None:  # если список пустой, то выйти
            return
        node = prev = self.head  # текущий и предыдущий узел начинаются с "головы"
        
        while node:
            if node == self.head and node.value == val:  # Удаление первого узла 
                self.head = self.head.next
                node = self.head
                prev = self.head
                if all is False:
                    break
                continue
            
            node = prev.next  # 
            if node != None and node.value == val:  # Удаляем все остальные узлы 
                prev.next = node.next  # Перепривязываем ссылку на след.узел
                node = prev
                if all is False:
                    break
            else:
                prev = prev.next
                node = prev
            
        node = self.head  # переопределяем хвост
        self.tail = None
        while node:
            self.tail = node
            node = node.next
        return

    def clean(self):  # 1.3. Добавьте в класс LinkedList метод очистки всего содержимого (создание пустого списка)
        # self.head = self.tail.next
        self.__init__()
        # self.head = None
        # self.tail = None

    def len(self): # 1.5. Добавьте в класс LinkedList метод вычисления текущей длины списка
        node = self.head
        l = 0
        while node:
            l += 1
            node = node.next
        return l # здесь будет ваш код

    def insert(self, afterNode, newNode): # 1.6. Добавьте в класс LinkedList метод вставки узла newNode после заданного узла afterNode (из списка)
        node = self.head

        while node:
            if node == afterNode:
                newNode.next = node.next
                node.next = newNode
                if newNode.next is None:
                    self.tail = newNode
                return
            node = node.next

        newNode.next = self.head
        self.head = newNode

# n1 = Node(12)
# n2 = Node(999)
# n1.next = n2 # 12 -> 55
# s_list = LinkedList()
# s_list.add_in_tail(n1)
# s_list.add_in_tail(n2)
# s_list.add_in_tail(Node(55))
# s_list.add_in_tail(Node(12))
# s_list.add_in_tail(Node(55))
# s_list.add_in_tail(Node(33))
# s_list.add_in_tail(Node(12))
# print('Начальные список')
# s_list.print_all_nodes()

# 1.1. Добавьте в класс LinkedList метод удаления одного узла по его значению
# s_list.delete(12, True)
# print('Удалить 12')
# print('последний элемент', s_list.head, s_list.tail.value)
# s_list.print_all_nodes()

# # 1.2. Дополните этот метод удалением всех узлов по конкретному значению (флажок all=True)
# s_list.delete(128, True)
# print('Удалить все 128')
# print('последний элемент', s_list.tail.value)  
# s_list.print_all_nodes()

# # 1.3. Добавьте в класс LinkedList метод очистки всего содержимого (создание пустого списка)
# s_list.clean()
# print('Очистить всё')

# 1.4. Добавьте в класс LinkedList метод поиска всех узлов по конкретному значению (возвращается стандартный питоновский список найденных узлов).
# print(s_list.find_all(12))

# # 1.5. Добавьте в класс LinkedList метод вычисления текущей длины списка
# print('Длина списка: ', s_list.len())

# 1.6. Добавьте в класс LinkedList метод вставки узла newNode после заданного узла afterNode (из списка)
# s_list.insert(n1, Node(3))
# print('Вставить новый узел')
# s_list.print_all_nodes()
