import unittest
import leapYear

class testYear(unittest.TestCase):
   
    def setUp(self):
        self.yearTrue=leapYear.leap(1996)
        self.yearFalse=leapYear.leap(2002)

    def test_leap(self):
        self.assertEqual(self.yearFalse,False,"should be False")

    def test_leapF(self):
        self.assertEqual(self.yearTrue,True,"should be True")

    def tearDown(self):
        return super().tearDown()

if __name__=="__main__":
    unittest.main()