import unittest
from Level_5_10 import PowerSet

class DefTest(unittest.TestCase):

    def setUp(self):
        self.ps = PowerSet()
        for i in range(20):
            self.ps.put('test' + str(i))
        self.set2 = {}
        self.set3 = {}
        for i in range(0, 10, 2):
            self.ps.put('test1' + str(i))

        set_ps = []    
        for i in range(20):
            set_ps.append('test' + str(i))
        self.set_ps = set(set_ps)

    def test1(self): # добавление 10 000 эл-ов
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
        # set2 = ['test2', 'test22', 'test5', 'test55', 'test3']
        res = self.ps.intersection({'test22', 'test51', 'test55'})
        self.assertEqual(res, None)
    
    def test4(self): # объединение union(), когда оба параметра непустые, и когда один из параметров -- пустое множество;
        res = self.ps.union(self.set2)
        self.assertEqual(res, self.ps.get_set())
    
    def test5(self): # разница difference(), чтобы в результате получались как пустое, так и непустое множества;
        res = self.ps.difference(self.set_ps)
        self.assertEqual(res, None)

        res1 = self.ps.difference({'test22', 'test4', 'test6', 'test88', 'test10', 'test12', 'test14', 'test16', 'test18'})
        self.assertEqual(res1, {'test22', 'test88'})

    def test5(self):
        res1 = self.ps.issubset(self.set_ps)  # все элементы параметра входят в текущее множество
        self.assertEqual(res1, True)
        
        set_ps = list(self.set_ps)
        set_ps.append('test555')
        set_ps.append('test888')
        self.set_ps = set(set_ps)
        res2 = self.ps.issubset(self.set_ps) # все элементы текущего множества входят в параметр
        self.assertEqual(res2, False)
        
        set_ps = list(self.set_ps)
        set_ps.remove('test18')
        self.set_ps = set(set_ps)
        res3 = self.ps.issubset(self.set_ps)  # не все элементы параметра входят в текущее множество
        self.assertEqual(res3, False)

if __name__ == '__main__':
    unittest.main()