import unittest
from Level_5_7 import OrderedList, OrderedStringList

class DefTest(unittest.TestCase):

    def setUp(self):
        self.n1_list = OrderedList()
        
        self.n2_list = OrderedList()
        self.n2_list.add(1)

        self.n3_list = OrderedList()
        for i in range(100):
            self.n3_list.add(i)

        self.s1_list = OrderedStringList()

        self.s2_list = OrderedList()
        self.s2_list.add(1)

        self.s3_list = OrderedList()
        for i in range(100):
            self.s3_list.add(i)

    def test_1(self): # добавление элементов
        # добавление в пустой список
        self.n1_list.add(5)
        res1 = self.n1_list.head.value
        res2 = self.n1_list.tail.value
        self.assertEqual(res1, 5)
        self.assertEqual(res2, 5)
    
        # добавление в список с одним узлом
        self.n2_list.add(5)
        res3 = self.n2_list.head.value
        res4 = self.n2_list.tail.value
        self.assertEqual(res3, 1)
        self.assertEqual(res4, 5)

        # добавление в список со 100 узлами
        self.n3_list.add(5)
        res5 = self.n3_list.head.value
        res6 = self.n3_list.tail.value
        self.assertEqual(res5, 0)
        self.assertEqual(res6, 99)

    def test_2(self): # удаление элементов
        # удаление из пустого списка
        self.n1_list.delete(5)
        res1 = self.n1_list.head
        res2 = self.n1_list.tail
        self.assertEqual(res1, None)
        self.assertEqual(res2, None)
    
        # удаление из списка с одним узлом
        self.n2_list.delete(1)
        res3 = self.n2_list.head
        res4 = self.n2_list.tail
        self.assertEqual(res3, None)
        self.assertEqual(res4, None)

        # добавление в список со 100 узлами
        self.n3_list.delete(5)
        res5 = self.n3_list.head.value
        res6 = self.n3_list.tail.value
        self.assertEqual(res5, 0)
        self.assertEqual(res6, 99)

    def test3(self): # поиск элементов
        # поиск в пустом списке
        res0 = self.n1_list.find(5)
        self.assertEqual(res0, None)
    
        # поиск в списке с одним узлом
        res0 = self.n2_list.find(5)
        self.assertEqual(res0, None)
    
        # поиск в списке со 100 узлами
        res0 = self.n3_list.find(5)
        self.assertEqual(res0.value, 5)
    
if __name__ == '__main__':
    unittest.main()