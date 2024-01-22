#! /usr/bin/env python3

"""
unittesting statistics solution
"""

__author__ = "Benjamin Robillard"

import unittest
from stats import solution

class TestStatistics(unittest.TestCase):
    def test1_answer(self):
        self.assertEqual(solution(['2', '6', '9']), "6 9 3")
    def test2_answer(self):
        self.assertEqual(solution(['2', '1', '2']), "1 2 1")
    def test3_answer(self):
        self.assertEqual(solution(['2', '0', '9']), "0 9 9")
    def test4_answer(self):
        self.assertEqual(solution(['3', '4', '9', '2']), "2 9 7")
    def test5_answer(self):
        self.assertEqual(solution(['1', '4']), "4 4 0")
    def test6_answer(self):
        self.assertEqual(solution(['8', '1', '2', '3', '4', '5', '6', '7', '8']), "1 8 7")                                                               
    
    print("All test cases passed...")


if __name__ == "__main__":
    unittest.main(verbosity=2)