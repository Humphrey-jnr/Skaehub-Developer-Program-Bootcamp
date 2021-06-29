import unittest
from duplicates import *

class test_duplicates(unittest.TestCase):
    def test_data(self):
        self.assertEqual(type(thislist), list,"should be list")

    def test_data2(self):
        self.assertEqual(type(thislist2), dict,"should be dict")

    def test_duplicate(self):
        self.assertEqual(thislist,thislist3,"should not be equal")


if __name__=="__main__":
    unittest.main()