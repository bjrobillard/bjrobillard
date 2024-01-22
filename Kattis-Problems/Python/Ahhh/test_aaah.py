#! /usr/bin/env python3

"""
unittesting Aaah solution
"""

__author__ = "Benjamin Robillard"

import unittest
from aaah import solution

class TestAaah(unittest.TestCase):
    def test1_answer(self):
        self.assertEqual(solution("aah", "aaaaaah"), "no", "wrong")
    def test2_answer(self):
        self.assertEqual(solution("aaaaaaaah", "aaaaaah"), "go", "wrong")
    def test3_answer(self):
        self.assertEqual(solution("ah", "aaaaaaaaaaaah"), "no", "wrong")
    def test4_answer(self):
        self.assertEqual(solution("aaaaaaaaah", "aaaaaah"), "go", "wrong")
    def test5_answer(self):
        self.assertEqual(solution("aaaaaaaaaaah", "aaaaaaah"), "go", "wrong")
    def test6_answer(self):
        self.assertEqual(solution("aah", "aaaaaah"), "no", "wrong")
    

if __name__ == "__main__":
    unittest.main(verbosity=2)