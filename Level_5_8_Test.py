import unittest
from Level_5_8 import HashTable

class DefTest(unittest.TestCase):
    def setUp(self):
        self.ht1 = HashTable(0, 0)

        self.ht2 = HashTable(1, 1)
        self.ht2.put('1')

        self.ht3 = HashTable(128, 3)
        for i in range(0, 63, 2):
            self.ht3.put('i')
        
    def test1(self):
        res1 = self.ht3.hash_fun('3')
        self.assertEqual(res1, 51)

    def test2(self):
        res1 = self.ht3.seek_slot('3')
        self.assertEqual(res1, 51)

    def test3(self):
        res1 = self.ht3.put('4')
        self.assertEqual(res1, 73)

    def test4(self):
        res1 = self.ht3.find('300')
        self.assertEqual(res1, 52)
    
if __name__ == '__main__':
    unittest.main()