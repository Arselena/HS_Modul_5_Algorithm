import unittest
from Level_5_6 import Deque

class DefTest(unittest.TestCase):

    def setUp(self):
        self.deq_1 = Deque()

        self.deq_2 = Deque()
        self.deq_2.addTail(1)

        self.deq_3 = Deque()
        for i in range(100):
            self.deq_3.addTail(i)
    
    def test_1(self):  # проверим методы addFront()
        # вставка в пустой список
        self.deq_1.addFront("f1")
        res1 = self.deq_1.deque[0]
        self.assertEqual(res1, "f1")
        res_s = self.deq_1.size()
        self.assertEqual(res_s, 1)

        # вставка в список с 1 эл-ом
        self.deq_2.addFront("f2")
        res2 = self.deq_2.deque[0]
        self.assertEqual(res2, "f2")
        res_s = self.deq_2.size()
        self.assertEqual(res_s, 2)

        # вставка в список с 100 эл.
        self.deq_3.addFront("f3")
        res3 = self.deq_3.deque[0]
        self.assertEqual(res3, "f3")
        res_s = self.deq_3.size()
        self.assertEqual(res_s, 101)

    def test_2(self):  # проверим методы addTail()
        # вставка в пустой список
        self.deq_1.addTail("t1")
        res1 = self.deq_1.deque[0]
        self.assertEqual(res1, "t1")
        res_s = self.deq_1.size()
        self.assertEqual(res_s, 1)

        # вставка в список с 1 эл-ом
        self.deq_2.addTail("t2")
        res2 = self.deq_2.deque[1]
        self.assertEqual(res2, "t2")
        res_s = self.deq_2.size()
        self.assertEqual(res_s, 2)

        # вставка в список с 100 эл.
        self.deq_3.addTail("t3")
        res3 = self.deq_3.deque[100]
        self.assertEqual(res3, "t3")
        res_s = self.deq_3.size()
        self.assertEqual(res_s, 101)

    def test_3(self):  # проверим методы removeFront()
        # удаление из пустого списка
        res11 = self.deq_1.removeFront()
        self.assertEqual(res11, None)
        res_s = self.deq_1.size()
        self.assertEqual(res_s, 0)

        # удаление из списка с 1 эл-ом
        res22 = self.deq_2.removeFront()
        self.assertEqual(res22, 1)
        res_s = self.deq_2.size()
        self.assertEqual(res_s, 0)

        # удаление из списка со 100 эл.
        res33 = self.deq_3.removeFront()
        res3 = self.deq_3.deque[0]
        self.assertEqual(res33, 0)
        self.assertEqual(res3, 1)
        res_s = self.deq_3.size()
        self.assertEqual(res_s, 99)

    def test_3(self):  # проверим методы removeTail()
         # удаление из пустого списка
        res11 = self.deq_1.removeTail()
        self.assertEqual(res11, None)
        res_s = self.deq_1.size()
        self.assertEqual(res_s, 0)

        # удаление из списка с 1 эл-ом
        res22 = self.deq_2.removeTail()
        self.assertEqual(res22, 1)
        res_s = self.deq_2.size()
        self.assertEqual(res_s, 0)

        # удаление из списка со 100 эл.
        res33 = self.deq_3.removeTail()
        self.assertEqual(res33, 99)
        res_s = self.deq_3.size()
        self.assertEqual(res_s, 99)

if __name__ == '__main__':
    unittest.main()