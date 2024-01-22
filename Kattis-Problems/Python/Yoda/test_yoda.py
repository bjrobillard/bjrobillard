#! /usr/bin/env python3

"""
unittesting YODA solution
"""

__author__ = "Benjamin Robillard"

import unittest
from yoda import answer

class TestYoda(unittest.TestCase):
    def test1_answer(self):
        self.assertEqual(answer(123, 456), ("YODA", 456), "wrong")
    
    def test2_answer(self):
        self.assertEqual(answer(454, 626), (5, 66), "wrong")
    
    def test3_answer(self):
        self.assertEqual(answer(5000, 2111), (5, 111), "wrong")
    
    def test4_answer(self):
        self.assertEqual(answer(618, 777), (8, 77), "wrong")
    
    def test5_answer(self):
        self.assertEqual(answer(12, 401), (12, 4), "wrong")
    
    def test6_answer(self):
        self.assertEqual(answer(56700, 12), (567, 12), "wrong")
    
    print("All test cases passed...")


if __name__ == "__main__":
    unittest.main(verbosity=2)