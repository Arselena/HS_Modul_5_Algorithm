import unittest
from Level_5_10 import PowerSet

class DefTest(unittest.TestCase):

    def setUp(self):
        self.ps = PowerSet()
        for i in range(20):
            self.ps.put('test' + str(i))
        
        self.ps1 = PowerSet()  
        for i in range(40):
            self.ps1.put('test' + str(i))

        self.set0 = PowerSet()  # пустое множество

        self.set1 = PowerSet()  # дубликат множества ps
        for i in range(20):
            self.set1.put('test' + str(i))
           
        self.set2 = PowerSet()
        for i in range(0, 40, 2): # с ps совпадают четные значения до 19 и далее еще в диапазоне 20-40 с шагом 2
            self.set2.put('test' + str(i))

        self.set3 = PowerSet()
        for i in range(20, 40, 2): # с ps не совпадают
            self.set3.put('test' + str(i))

    def test1(self): # добавление 20 000 эл-ов
        for i in range(20000):
            self.ps.put(str(i))
        self.assertTrue(self.ps)

    def test2(self): # удаление элемента
        self.ps.remove('test5')
        res = self.ps.get('test5')
        self.assertEqual(res, False)

        self.ps.remove('')
        res1 = self.ps.get('test4')
        self.assertEqual(res1, True)

    def test3(self):  # пересечение множеств intersection(), чтобы в результате получались как пустое, так и непустое множества;
        res = self.ps.intersection(self.set1) # множества полностью совпадают
        self.assertCountEqual(res, self.ps.get_set())

        res1 = self.ps.intersection(self.set2) # множества частично пересекаются
        self.assertCountEqual(res1, {'test0', 'test2', 'test4', 'test6', 'test8', 'test10', 'test12', 'test14', 'test16', 'test18'}) 
        # assertCountEqual(a, b) — a и b содержат те же элементы в одинаковых количествах, но порядок не важен

        res2 = self.ps.intersection(self.set3) # множества не пересекаются
        self.assertEqual(res2, {})

    def test4(self): # объединение union(), когда оба параметра непустые, и когда один из параметров -- пустое множество;
        res = self.ps.union(self.set0) # не пустое с пустым
        self.assertEqual(res, self.ps.get_set())

        res1 = self.ps.union(self.set2) # не пустое с не пустым 
        self.assertCountEqual(res1, {'test0', 'test1', 'test2', 'test3', 'test4', 'test5', 'test6', 'test7', 'test8', 'test9', 'test10', 'test11', 'test12', 'test13', 'test14', 'test15', 'test16', 'test17', 'test18', 'test19', 'test20', \
            'test22', 'test24', 'test26', 'test28', 'test30', 'test32', 'test34', 'test36', 'test38'})

        res3 = self.set0.union(self.set2) # пустое множество с непустым
        self.assertCountEqual(res3, self.set2.get_set())

    def test5(self): # разница difference(), чтобы в результате получались как пустое, так и непустое множества;
        res = self.ps.difference(self.set1) # 
        self.assertEqual(res, {})

        res1 = self.ps.difference(self.set2)
        self.assertCountEqual(res1, {'test20', 'test22', 'test24', 'test26', 'test28', 'test30', 'test32', 'test34', 'test36', 'test38'})

    def test6(self): # вхождение множества 
        res1 = self.ps.issubset(self.set1)  # все элементы параметра входят в текущее множество
        self.assertEqual(res1, True)

        res2 = self.ps.issubset(self.ps1) # все элементы текущего множества входят в параметр
        self.assertEqual(res2, False)
        
        res3 = self.ps.issubset(self.set3)  # не все элементы параметра входят в текущее множество
        self.assertEqual(res3, False)

if __name__ == '__main__':
    unittest.main()