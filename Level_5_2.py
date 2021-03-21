# 2. Двунаправленный связный (связанный) список
class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class LinkedList2:  
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item

    def print_all_nodes(self): # метод отладочного вывода списка
        node = self.head
        while node != None:
            print(node.value)
            node = node.next

    def find(self, val):  # 2.1. метод поиска первого узла по его значению
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None # здесь будет ваш код

    def find_all(self, val):  # 2.2. метод поиска всех узлов по конкретному значению (возвращается список найденных узлов).
        s = []
        node = self.head
        while node is not None:
            if node.value == val:
                s.append(node)
            node = node.next
        return s

    def delete(self, val, all=False): # 2.3. метод удаления одного узла по его значению.
                                      # 2.4. Дополните этот метод удалением всех узлов по конкретному значению (флажок all=True).
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

    def clean(self):  # 2.7. метод очистки всего содержимого (создание пустого списка) -- clean()
        self.__init__()
        pass

    def len(self):  # 2.8. метод вычисления текущей длины списка -- len()
        node = self.head
        l = 0
        while node:
            l +=1
            node = node.next
        return l

    def insert(self, afterNode, newNode):   # 2.5. метод вставки узла после заданного узла.
                                            # 2.5.1. Если afterNode = None и список пустой, добавьте новый элемент первым в списке.
                                            # 2.5.2. Если afterNode = None и список непустой, добавьте новый элемент последним в списке.
        if (self.head is None) or (afterNode is None):  # условие для 2.5.1 и 2.5.2
            self.add_in_tail(newNode)
            return
        
        node = self.head
        while node:
            if node == afterNode:
                newNode.next = node.next
                node.next = newNode
                newNode.prev = node
                if afterNode == self.tail:
                    self.tail = newNode
                else:
                    newNode.next.prev = newNode
                return
            node = node.next
        
        pass # здесь будет ваш код

    def add_in_head(self, newNode):  # 2.6. метод вставки узла самым первым элементом.
        if self.head is None:  # если список пустой, то переопределить противоположный узел (хвост)
            self.tail = newNode
        elif self.head == self.tail:  # если один узел, то переопределить (пред.ИЛИ след.) узел у (хвоста ИЛИ головы) соответственно
            self.tail.prev = newNode
        else:
            newNode.next = self.head 
            self.head.prev = newNode  # если больше 2х узлоа, то переопределить (пред.ИЛИ след.) узел у (головы ИЛИ хвоста) соответственно
        newNode.prev = None
        self.head = newNode
        pass # здесь будет ваш код   

# n1 = Node(12)
# n2 = Node(13)
# n1.next = n2 # 12 -> 55
# n2.prev = n1
# s_list = LinkedList2()
# s_list.add_in_tail(n1)
# s_list.add_in_tail(n2)
# s_list.add_in_tail(Node(55))
# s_list.add_in_tail(Node(12))
# s_list.add_in_tail(Node(55))
# s_list.add_in_tail(Node(33))
# s_list.add_in_tail(Node(129))
# s_list.add_in_tail(Node(12))
# print('Начальные список')
# s_list.print_all_nodes()

# 2.1. метод поиска первого узла по его значению
# print("Поиск узла по значению", s_list.find(129).value)

# 2.2. метод поиска всех узлов по конкретному значению (возвращается список найденных узлов).
# print("Поиск всех узлов", s_list.find_all(12))

# 2.3. метод удаления одного узла по его значению
# 2.4. Дополните этот метод удалением всех узлов по конкретному значению (флажок all=True)
# s_list.delete(12, False)
# print('Удалить 12')
# # print('последний элемент', s_list.head.value)
# s_list.print_all_nodes()
# print(s_list.head.prev, s_list.tail.next)

# 2.5. метод вставки узла после заданного узла.
# s_list.insert(n1, Node(3))
# print('Вставить новый узел')
# s_list.print_all_nodes()

# 2.6. метод вставки узла самым первым элементом.
# s_list.add_in_head(Node(66))
# print('ADD in head')
# s_list.print_all_nodes()
# print(s_list.head.next.value, s_list.tail.value)

# 2.7. метод очистки всего содержимого (создание пустого списка) -- clean()
# s_list.clean()
# print('Очистить')
# s_list.print_all_nodes()

# 2.8. метод вычисления текущей длины списка -- len()
# print("длина списка:", s_list.len())