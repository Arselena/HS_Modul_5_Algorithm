# 4. Стек
# push - "втолкнуть" элемент в стек
# pop - извлечь последний втолкнутый в стек элемент. 
# peek() - получить верхний элемент стека, но не удалять его.

import ctypes
    
class Stack:
    def __init__(self):
        self.stack = []

    def make_stack(self, new_capacity):
        return (new_capacity * ctypes.py_object)()
    
    def size(self):
        return len(self.stack)

    def pop(self):
        size = self.size()
        if size == 0:
            return None # если стек пустой
        new_stack = ((self.size() - 1) * ctypes.py_object)()
        for i in range(size - 1):
            new_stack[i] = self.stack[i]
        end_element = self.stack[size - 1]
        self.stack = new_stack
        return end_element

    def push(self, value):
        new_stack = ((self.size() + 1) * ctypes.py_object)()  # расширяем массив памяти на 1 ячейку
        size = self.size()
        for i in range(size):
            new_stack[i] = self.stack[i]
        new_stack[size] = value
        self.stack = new_stack

    def peek(self):
        size = self.size()
        if size == 0:
            return None # если стек пустой
        return self.stack[size - 1]

    def print_all(self):
        for i in range(self.size()):
            print(self.stack[i])
# Переделайте реализацию стека так, чтобы она работала не с хвостом списка как с верхушкой стека, а с его головой.
    def pop_head(self):
        size = self.size()
        if size == 0:
            return None # если стек пустой
        new_stack = ((self.size() - 1) * ctypes.py_object)()
        for i in range(1, size):
            new_stack[i-1] = self.stack[i]
        head_element = self.stack[0]
        self.stack = new_stack
        return head_element

    def push_head(self, value):
        new_stack = ((self.size() + 1) * ctypes.py_object)()  # расширяем массив памяти на 1 ячейку
        new_stack[0] = value
        size = self.size()
        for i in range(1, size + 1):
            new_stack[i] = self.stack[i-1]
        self.stack = new_stack

    def peek_head(self):
        size = self.size()
        if size == 0:
            return None # если стек пустой
        return self.stack[0]

def Parentheses(s:str):
    st = Stack()
    for i in range(len(s)):
        if s[i] == '(':
            st.push(1)
        elif st.pop() == None:
            return 'Увы. Скобочная последовательность не сбалансирована'
    if st.size() == 0:
        return 'Да. Скобочная последовательность сбалансирована'
    return 'Увы. Скобочная последовательность не сбалансирована'

def isint(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def calculation(s:str):
    st1 = Stack()
    st2 = Stack()
    for i in range(len(s)): # наполняем 1-ый стек
        st1.push(s[i])
    while st1.size() > 0:
        if isint(st1.peek_head()) == True:
            st2.push_head(st1.pop_head())  # если число, то добавляем во 2ой стек
        else:
            if st1.peek_head() == '+':
                res = int(st2.pop_head()) + int(st2.pop_head())
            if st1.peek_head() == '-':
                res = int(st2.pop_head()) - int(st2.pop_head())
            if st1.peek_head() == '*':
                res = int(st2.pop_head()) * int(st2.pop_head())
            if st1.peek_head() == '/':
                res = int(st2.pop_head()) / int(st2.pop_head())
            st1.pop_head()
            st2.push_head(res)
    return st2.peek_head()

# print(Parentheses(''))
# print(calculation('82+5*9+'))
# st = Stack()
# st.push_head(1)
# st.push_head(2)
# st.push_head(3)
# print('первый эл-т', st.pop())
# print(st.size())
# st.push(1)
# st.push(2)
# st.push(3)
# st.print_all()
# print('первый эл-т', st.pop_head())
# print('первый эл-т', st.peek_head())
# print(st.pop())
# st.print_all()
# print(st.peek())
# st.print_all()

# Мера сложности для pop и push - O(n) зависит от размера массива, т.к. идет поэлементное копироварие в новый массив 