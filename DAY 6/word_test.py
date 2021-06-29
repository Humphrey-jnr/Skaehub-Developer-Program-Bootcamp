import unittest
from unittest.case import TestCase
from word_length import *


class test_split(unittest.TestCase):
    def test_word(self):
        #test for entered word
        self.assertEqual((word),"He is good", "should be He is good")

    def test_splitter(self):
        #testing with "He is good"
        self.assertEqual(word.split(), ['He','is','good'])
        

    def test_length(self):
        #test for length of last word
        self.assertEqual(len(list), 3,"should be 3")
        



if __name__=="__main__":
    unittest.main()