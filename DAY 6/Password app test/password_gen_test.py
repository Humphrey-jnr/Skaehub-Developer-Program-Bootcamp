import unittest
from password_generator import *

class test_password(unittest.TestCase):
    
    if opt==3:
        global lower1
        lower1=any(list(lower))

        password=list(password)
        def test_password(self):
            self.assertTrue(lower1,password)

    elif opt==2:
        global symb1
        symb1=any(list(symbols))

        password=list(password)
        def test_password(self):
            self.assertFalse(symb1,password)

    else:
        symb1=any(list(symbols))

        password=list(password)
        def test_password(self):
            self.assertTrue(symb1,password)
        

if __name__=="__main__":
    unittest.main()
    