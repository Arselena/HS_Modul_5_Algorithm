import unittest
from Level_5_12 import NativeCache

class DefTest(unittest.TestCase):

    def setUp(self):
        self.nc = NativeCache(17)
        for i in range(17):
            self.nc.put('ключ '+str(i), str(i*10))
            self.nc.get('ключ '+str(i))

    def test1(self): # добавление 200 эл-ов
        nc1 = NativeCache(17)
        for i in range(200):
            nc1.put('ключ '+str(i), str(i*10))
        self.assertTrue(nc1)

    def test2(self): # замена значения по существующему ключу
        self.nc.put('ключ 5', 'aaa')
        res = self.nc.get('ключ 5')
        self.assertEqual(res, 'aaa')

    def test3(self): # обращения к ф-ии get
        self.nc.put('ключ 55', '555')
        self.nc.get('ключ 55')
        self.nc.get('ключ 55')

        self.nc.put('ключ 77', '777')
        self.nc.get('ключ 77')
        self.nc.get('ключ 77')
        self.nc.get('ключ 77')

        res = self.nc.hits
        self.assertEqual(res, [2,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])

        res2 = self.nc.get('ключ 77')
        self.assertEqual(res2, '777')
    
    def test4(self): # обращения к ф-ии get
        for i in range(16, 34):  # все значения должны перезаписываться в 0 слот
            self.nc.put('ключ '+str(i), str(i*10))
        
        res = self.nc.slots[0]
        self.assertEqual(res, 'ключ 33')
        
        res2 = self.nc.hits  # кол-во обращений по новому эл-у обнуляется
        self.assertEqual(res2, [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])

if __name__ == '__main__':
    unittest.main()