from __future__ import annotations

__author__ = "Benjamin Robillard"
__Kattis_Problem__ = "Mixed Fractions Kattis"
__assignment__ = "Assignment 5"
__class__ = "CSCI 375 - 001"

import unittest
from mixedFractions import MixedFractions
from hypothesis import given
import hypothesis.strategies as some

from fractions import Fraction

class TestMixedFractions(unittest.TestCase):
    @given(some.tuples(some.integers(max_value=2147483648), some.integers(max_value=2147483648)))
    def test_find_mixFrac_retType(self, inpt):
        """ Testing function used to test the correct output type of find_mixFrac using the hypothesis module to test against 
        different inputs

        Args:
            inpt (tuple[int,int]): hypothesis input of a bunch of different improper fractions 
        """
        mixFrac = MixedFractions(inpt[0], inpt[1])
        self.assertIsInstance(mixFrac.find_mixFrac(), str)
    
    @given(some.tuples(some.integers(min_value=1, max_value=2147483648), some.integers(min_value=1, max_value=2147483648)))
    def test_find_mixFrac(self, inpt):
        """ Testing function used to test that find_mixFrac is outputting the correct mixed fraction from the inputted 
        improper fraction given from the hypothesis class

        Args:
            inpt (tuple[int,int]): hypothesis input of a bunch of different improper fractions used for testing
        """
        mixFrac = MixedFractions(inpt[0], inpt[1])
        frac = Fraction(inpt[0], inpt[1], _normalize=False)
        n, d = (frac.numerator, frac.denominator)
        m, p = divmod(abs(n), d)
        newFrac = "{} {} / {}".format(m, p, d)
        self.assertEqual(mixFrac.find_mixFrac(), newFrac)

if __name__ == "__main__":
    unittest.main(verbosity=2)