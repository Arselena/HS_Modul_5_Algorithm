# 5.3. Динамические массивы
import ctypes

class DynArray:
    
    def __init__(self):
        self.count = 0  # текущее количество элементов в массиве
        self.capacity = 16  # текущая ёмкость буфера
        self.array = self.make_array(self.capacity)  # указатель на блок памяти нужной ёмкости, хранящий элементы PyObject

# Пример: мы хотим сформировать блок оперативной памяти, где собираемся хранить последовательность значений (объектов). Для этого надо выполнить команду
# (N * ctypes.py_object)()
# которая отведёт в памяти N ячеек, предназначенных для хранения объектов (точнее, ссылок на объекты) Python.
# import ctypes
# A = (3 * ctypes.py_object)()
# Теперь мы можем обращаться к A как к адресуемой области памяти! Фактически, Python разрешает нам индексировать эту область напрямую:
# A[0] = 1024
# A[1] = '1024'
# A[2] = 10.24
# Более того, A поддерживает перечисление, то есть допускается такая запись:
# for i in A:
#     print(i)

    def __len__(self):
        return self.count

    def make_array(self, new_capacity): # выделяем блок ОЗУ, где собираемся хранить данные
        return (new_capacity * ctypes.py_object)()

# Стандартный метод __getitem__() обеспечивает поддержку индексации нашего класса. 
# В неё мы встроим проверку корректности индекса в рамках границ, и генерацию соответствующего исключения.
    def __getitem__(self,i):
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')
        return self.array[i]

# Ключевой метод resize(), меняющий размер внутреннего буфера, 
# просто формирует через make_array() новый буфер, и копирует в него текущее содержимое.
    def resize(self, new_capacity):
        new_array = self.make_array(new_capacity)
        for i in range(self.count):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

# Наконец, метод append() добавляет новый элемент в конец массива.
    def append(self, itm):
        if self.count == self.capacity:
            self.resize(2*self.capacity)
        self.array[self.count] = itm
        self.count += 1

    def insert(self, i, itm): # 5.1. добавляем объект itm в позицию i, начиная с 0
        if self.count == 0 and i == 0:
            self.append(itm)
            return
        elif i != 0:
            self[i-1]   # если индекс i лежит вне допустимых границ, генерируем исключение __getitem__. 
                    # Для вставки в конец: (i-1) не больше текущей длины массива
        if self.count == self.capacity:
            self.resize(2*self.capacity)
        new_array = self.make_array(self.capacity)
        a1 = 0
        for a2 in range(self.count + 1):
            if a2 == i:
                new_array[a2] = itm
                continue
            new_array[a2] = self.array[a1]
            a1 +=1
        self.array = new_array
        self.count +=1

    def delete(self, i): # удаляем объект в позиции i
        self[i]  # # если индекс i лежит вне допустимых границ, генерируем исключение __getitem__. 
        new_array = self.make_array(self.capacity)
        a1 = 0
        for a2 in range(self.count - 1):
            if a1 == i:
                a1 = i + 1
            new_array[a2] = self.array[a1]
            a1 += 1
        self.array = new_array
        self.count -=1

        if self.count < self.capacity / 2:
            new_capacity = int(self.capacity // 1.5)
            if new_capacity > 16:
                self.resize(new_capacity)
            else:
                self.resize(16)
        pass

    def print_all(self):
        for i in range(self.count):
            print(self[i])
        print('массив / память', self.count, self.capacity)

# da = DynArray()
# for i in range(1):
#     da.append(i)
#     print (da[i])
# print(da.count, da.capacity)
# da.insert(0, 22)
# da.print_all()
# da.delete(0)
# da.print_all()

# da.insert(2, 22)
# da.insert(2, 23)
# da.insert(2, 24)
# da.insert(2, 25)
# da.insert(2, 26)
# da.insert(2, 27)
# da.insert(2, 28)
# da.insert(2, 29)
# da.insert(2, 30)
# da.insert(2, 31)
# da.insert(2, 32)
# da.insert(26, 33)
# da.print_all()