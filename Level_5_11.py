# 11. Фильтр Блюма

class BloomFilter:

    def __init__(self, f_len):
        self.filter_len = f_len
        self.filters = 0

    def hash1(self, str1):
        # в качестве случайных чисел для первой функции используйте 17
        # организуем цикл до длины строки, результат в этом цикле считаем как его версия с предыдущей итерации, 
        # умноженная на случайное число, к которой прибавляется код очередного символа, и берём результат тут же по модулю длины таблицы.
        index = 0
        for c in str1:
            code = ord(c)  # Функция ord() для символа x вернет число, из таблицы символов Unicode представляющее его позицию. Например, ord('a') возвращает целое число 97 и ord('€') вернет 8364.
            index = (index * 17 + code) % self.filter_len
        return 0 | (1 << index) # возвращаем маску с 1 на месте индекса

    def hash2(self, str1):
        # 223 
        index = 0
        for c in str1:
            code = ord(c) 
            index = (index * 223 + code) % self.filter_len
        return 0 | (1 << index)

    def add(self, str1):
        # добавляем строку str1 в фильтр
        self.filters = self.filters | self.hash1(str1) # бинарное или
        self.filters = self.filters | self.hash2(str1)
        return self.filters

    def is_value(self, str1):
        # проверка, имеется ли строка str1 в фильтре
        mask = self.filters & (self.hash1(str1) | self.hash2(str1))
        if mask == self.hash1(str1) | self.hash2(str1):
            return True
        return False
        
# bl = BloomFilter(32)

# x = "0123456789"
# for i in range(9):
#     bl.add(x)
#     x = x[1:] + x[0]

# print(bin(bl.filters))
# x = "0123456789"
# for i in range(9):
#     print(bl.is_value(x))
#     x = x[1:] + x[0]
# print(bl.is_value("0213456789"))