from __future__ import annotations

__author__ = "Benjamin Robillard"
__Kattis_Problem__ = "Mixed Fractions Kattis"
__assignment__ = "Assignment 5"
__class__ = "CSCI 375 - 001"

import unittest
from stats import Statistics, BaseStatistics
from hypothesis import given
import hypothesis.strategies as some
import math


class TestStatistics(unittest.TestCase):
    @given(some.lists(some.integers(min_value=-1000000, max_value=1000000), min_size=3, max_size=30))
    def test_find_range(self, inpt):
        """ testing that the find_range function of Statistics is working correctly and finding the correct range

        Args:
            inpt (list[int]): data set vals from -1000000 and 1000000
        """
        rangeVal = max(inpt[1:]) - min(inpt[1:])
        findRangeVal =  Statistics(inpt)
        self.assertEqual(findRangeVal.find_range(), rangeVal)
        
    @given(some.lists(some.integers(min_value=-1000000, max_value=1000000), min_size=3, max_size=30))
    def test_find_stats(self, inpt):
        """ testing find_stats() function such that it's outputting the correct format of the stats

        Args:
            inpt (list[int]): data set vals from -1000000 and 1000000
        """
        rangeVal = max(inpt[1:]) - min(inpt[1:])
        maxVal = max(inpt[1:])
        minVal = min(inpt[1:])
        statsVals = str(minVal) + " " + str(maxVal) + " " + str(rangeVal)
        findRangeVal =  Statistics(inpt)
        self.assertEqual(findRangeVal.find_stats(), statsVals)

class TestBaseStatistics(unittest.TestCase):
    @given(some.lists(some.integers(min_value=-1000000, max_value=1000000), min_size=3, max_size=30))
    def test_find_max(self, inpt):
        """ testing find_max() function of BaseStatistics so that it's outputting the correct number

        Args:
            inpt (list[int]): data set of vals from -1000000 and 1000000
        """
        maxVal = max(inpt[1:])
        findMaxVal = BaseStatistics(inpt)
        self.assertEqual(findMaxVal.find_max(), maxVal)
    
    @given(some.lists(some.integers(min_value=-1000000, max_value=1000000), min_size=3, max_size=30))
    def test_find_min(self, inpt):
        """ testing the BaseStatistics.find_min() is outputting correct ans

        Args:
            inpt (list[int]): data set of vals from -1000000 to 1000000
        """
        minVal = min(inpt[1:])
        findMinVal = BaseStatistics(inpt)
        self.assertEqual(findMinVal.find_min(), minVal)
    