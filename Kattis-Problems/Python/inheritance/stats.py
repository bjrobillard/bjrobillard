from __future__ import annotations

#! /usr/bin/env python

__author__ = "Benjamin Robillard"
__Kattis_Problem__ = "Statistics Kattis"
__assignment__ = "Assignment 6"
__class__ = "CSCI 375 - 001"

class BaseStatistics(object):
    def __init__(self, inputLine:list[int]) -> None:
        """ Initialize self._inputLine for BaseStatistics to use as the input data

        Args:
            inputLine (list): List of numbers to use to find the min, max, and range
        """
        self._inputLine:list[int] = inputLine

    def find_max(self) -> int:
        """ Method to find max value from the given input data

        Returns:
            int: Max value of the input data
        """
        maxNum = -1000000
        for i in self._inputLine[1:len(self._inputLine)]:
            if int(maxNum) <= int(i):
                maxNum = i
            else:
                maxNum = maxNum
        return maxNum

    def find_min(self) -> int:
        """ Method used to find the min value from the given input data

        Returns:
            int: Min value of the input data
        """
        minNum = 1000000
        for i in self._inputLine[1:len(self._inputLine)]:
            if int(minNum) >= int(i):
                minNum = i
            else:
                minNum = minNum
        return minNum


class Statistics(BaseStatistics):
    def __init__(self, inputLine:list[int]) -> None:
        """ Initialize the Class to use the given input data that BaseStatistics is given

        Args:
            inputLine (list): List of numbers 
        """
        super().__init__(inputLine)

    def find_range(self) -> int:
        """ Finding range of inputs using the find_min() and find_max() functions from BaseStatistics

        Returns:
            int: range from inputs
        """
        maxNum = self.find_max()
        minNum = self.find_min()
        rangeNum = int(maxNum) - int(minNum)
        return rangeNum

    def find_stats(self) -> str:
        """ Format stats gotten from find_range(), find_min(), and find_max() so that they're in the right
        order and separated by a space.

        Returns:
            str: min max range - from inputs given
        """
        maxNum = self.find_max()
        minNum = self.find_min()
        rangeNum = self.find_range()
        return str(minNum) + " " + str(maxNum) + " " + str(rangeNum)

