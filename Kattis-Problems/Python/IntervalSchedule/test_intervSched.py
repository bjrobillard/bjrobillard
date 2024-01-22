#! /usr/bin/env python3

"""
unittesting interval scheduling solution
"""

__author__ = "Benjamin Robillard"

import unittest
from intervSched import solution

class TestIntervSched(unittest.TestCase):
    def test1_answer(self):
        self.assertEqual(solution())
    def test2_answer(self):
        self.assertEqual(solution())
    def test3_answer(self):
        self.assertEqual(solution())
    def test4_answer(self):
        self.assertEqual(solution())
    def test5_answer(self):
        self.assertEqual(solution())
    def test6_answer(self):
        self.assertEqual(solution())
    
    print("All test cases passed...")


if __name__ == "__main__":
    unittest.main(verbosity=2)