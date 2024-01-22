from __future__ import annotations

__author__ = "Benjamin Robillard"
__class__ = "CSCI 375 - 001"
__assignment__ = "A7 Kattis Problem using ABC"

import unittest
from cup import Cup
from hypothesis import given
import hypothesis.strategies as some
import math

class TestCup(unittest.TestCase):
    """ Unittesting Cup Class
    """
    # list[int,list[str or int, str or int], ...]
    @given(some.tuples(some.integers(min_value=1, max_value=1000), some.characters(min_codepoint=1, max_codepoint=20)))
    def testing_is_int(self, inpt):
        """ Testing fxn to check if first element in list is an integer

        Args:
            inpt (list[int, str]): list containing the radius (first element) and color (second element)
        """
        sol = Cup(inpt)
        self.assertEqual(True, sol.is_int())

    @given(some.tuples(some.characters(min_codepoint=1, max_codepoint=20), some.integers(min_value=1, max_value=1000)))
    def testing_is_int_false(self, inpt):
        """ Testing fxn to check if first element in list is an int (it's not in this case)

        Args:
            inpt (list[str, int]): list containing the color (first element) and radius (second element) 
        """
        sol = Cup(inpt)
        self.assertEqual(False, sol.is_int())

    # @given(some.tuples(some.characters(min_codepoint=1, max_codepoint=20), some.integers(min_value=1, max_value=1000)))
    # def testing_str__(self, inpt):
    #     cup = Cup(inpt)
    #     self.assertIsInstance(str, type(cup.__str__()))