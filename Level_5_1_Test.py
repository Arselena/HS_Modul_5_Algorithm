import unittest
from Level_5_1 import Node, LinkedList

class DefTest(unittest.TestCase):

    def setUp(self):
        self.s1_list = LinkedList()

        self.s2_list = LinkedList()
        self.s2_list.add_in_tail(Node(12))

        self.s3_list = LinkedList()
        for i in range(1, 1000):
            self.s3_list.add_in_tail(Node(i))

    def test_1(self): # 1.1. Удаление одного узла по значению
        # Удаляем 128 из пустого списка
        self.s1_list.delete(128)
        self.assertEqual(self.s1_list.head, None)
        
        # Удаляем 128 из списка с одним узлом [12]
        self.s2_list.delete(128)
        self.assertTrue(self.s2_list)
        self.assertEqual(self.s2_list.head.value, 12)
        self.assertEqual(self.s2_list.tail.value, 12)

        # Удаляем 128 из списка с узлами от 1 до 1000
        self.s3_list.delete(128)
        self.assertTrue(self.s3_list)
        self.assertEqual(self.s3_list.head.value, 1)
        self.assertEqual(self.s3_list.tail.value, 999)
    
    def test_2(self): # 1.2. Удаление всех узлов по значению
        # Удаляем 12 из списка с одним узлом [12]
        self.s2_list.delete(12, True)
        self.assertTrue(self.s2_list)
        self.assertEqual(self.s2_list.head, None)
        self.assertEqual(self.s2_list.tail, None)

        # Удаляем 128 из списка с узлами от 1 до 1000
        self.s3_list.add_in_tail(Node(128))
        self.s3_list.add_in_tail(Node(128))

        self.s3_list.delete(128, True)
        self.assertTrue(self.s3_list)
        self.assertEqual(self.s3_list.head.value, 1)
        self.assertEqual(self.s3_list.tail.value, 999)
        self.assertEqual(self.s3_list.find_all(128), [])

    def test_3(self): # 1.3. метод очистки всего содержимого (создание пустого списка)
        self.s1_list.clean()
        self.assertTrue(self.s1_list)

        self.s2_list.clean()
        self.assertTrue(self.s2_list)

        self.s3_list.clean()
        self.assertTrue(self.s3_list)
        self.assertEqual(self.s3_list.head, None)
        self.assertEqual(self.s3_list.tail, None)

    def test_4(self): # 1.4. метод поиска всех узлов по конкретному значению
        res1 = self.s1_list.find_all(128)
        self.assertEqual(res1, [])

        res2 = self.s2_list.find_all(12)
        self.assertEqual(res2[0], self.s2_list.head)
        self.assertEqual(res2[0], self.s2_list.tail)

        self.s3_list.add_in_tail(Node(128))
        self.s3_list.add_in_tail(Node(128))
        res3 = self.s3_list.find_all(128)
        self.assertTrue(res3)
        self.assertEqual(len(res3), 3)

    def test_5(self): # 1.5. метод вычисления текущей длины списка
        self.assertEqual(self.s1_list.len(), 0)
        self.assertEqual(self.s2_list.len(), 1)
        self.assertEqual(self.s3_list.len(), 999)
    
    def test_6(self): # 1.6. метод вставки узла newNode после заданного узла afterNode (из списка)
        def create_list(s=LinkedList()): # создадим список узлов
            S = []
            node = s.head
            while node:
                S.append(node)
                node = node.next
            return S
        newNode = Node(999)

        res1 = create_list(self.s1_list)
        self.s1_list.insert(1, newNode)
        self.assertEqual(self.s1_list.head, newNode)

        res2 = create_list(self.s2_list)
        self.s2_list.insert(res2[0], newNode)
        self.assertEqual(self.s2_list.head.value, 12)
        self.assertEqual(self.s2_list.tail.value, 999)

        res3 = create_list(self.s3_list)
        self.s3_list.insert(res3[998], newNode)
        self.assertTrue(self.s3_list)
        self.assertEqual(res3[998].value, 999)
        self.assertEqual(res3[997].value, 998)
        self.assertEqual(self.s3_list.tail.value, 999)
        self.assertNotEqual(res3[998], self.s3_list.tail)

if __name__ == '__main__':
    unittest.main()