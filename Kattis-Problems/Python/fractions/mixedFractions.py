from __future__ import annotations

__author__ = "Benjamin Robillard"
__Kattis_Problem__ = "Mixed Fractions Kattis"
__assignment__ = "Assignment 5"
__class__ = "CSCI 375 - 001"

class MixedFractions(object):
    def __init__(self, numerator:int, denominator:int) -> None:
        """ Initializer used to initialize the numerator and denominator attributes of the input given

        Args:
            numerator (int): numerator given from the input (number from 1 - ((2^31)-1))
            denominator (int): denominator given from the input (number from 1 - ((2^31)-1))
        """
        self._numerator = numerator
        self._denominator = denominator

    def find_mixFrac(self) -> str:
        """ Method used to find and format the mixed fraction gotten from the input from Main class. Returns the mixed fraction
        in the format; {} {} / {}

        Returns:
            str: Formatted mixed fraction from the given numerator / denominator
        """
        if self._denominator == 0:
            return ""
        else:
            # print(self._numerator, self._denominator)
            a = self._numerator // self._denominator
            b = self._numerator % self._denominator
            return "{} {} / {}".format(a, b, self._denominator)
