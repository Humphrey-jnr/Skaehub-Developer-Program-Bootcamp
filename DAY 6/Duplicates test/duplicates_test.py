import unittest
import duplicates

class testDuplicates(unittest.TestCase):
    def test_type(self):
        self.assertEqual(type(duplicates.dict_list),dict,"Should be dict")
    def test_type2(self):
        self.assertIs(type(duplicates.list_final),list)

if __name__=="__main__":
    unittest.main()