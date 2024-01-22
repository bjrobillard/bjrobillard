from __future__ import annotations
#! usr/bin/env python

__author__ = "Benjamin Robillard"
__Kattis_Problem__ = "Title Cost Kattis"
__assignment__ = "Assignment 4"
__class__ = "CSCI 375 - 001"

class Hypothesis(object):
    """This is an class to handle initializing the title and title cost as well as using the find_cost() method to find the cost of the 
        title if it is less than the given budget

    Args:
        object: object class
    """
    def __init__(self, cost:float, title:str) -> None:
        """ Initialize the title and title cost for the find_cost function

        Args:
            cost (float): self._cost of the title given from input() and read_data() methods in Main class
            title (str): self._title of the given input - used to find if budget is surpassed or not
        """
        self._cost = cost
        self._title = title

    def find_cost(self) -> float:
        """ Method used to determine if self._title is longer than budget or not

        Returns:
            float: returns self._title (length) if length is less than the budget given; returns self._cost if title length
                is smaller than the budget
        """
        titleLen = self._title.__len__()
        if float(titleLen) > float(self._cost):
            # print(round(float(kattisInpt[1]), 8))
            return(float(self._cost))
        else: 
            return float(titleLen)

    def __str__(self) -> str:
        """ function to return the self._cost and self._title in human readable form

        Returns:
            str: returns (human readable) string representation of self._title and self._cost
        """
        return f"Cost: {self._cost}, Title: {self._title}"

    def __repr__(self) -> str:
        """ Function to return the self._cost and self._title in machine readable form

        Returns:
            str: Returns (machine readable) string representation of self._title and self._cost 
        """
        return self.__str__()