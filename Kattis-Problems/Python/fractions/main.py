from __future__ import annotations

__author__ = "Benjamin Robillard"
__Kattis_Problem__ = "Mixed Fractions Kattis"
__assignment__ = "Assignment 5"
__class__ = "CSCI 375 - 001"

import sys
from sys import stdin
from mixedFractions import MixedFractions

class Main(object):
    def __init__(self) -> None:
        """ Initializer for Main class - initializes self._inpt (list to store inputs from user/kattis) and self._ans (list to store
        answers to be written out)
        """
        self._inpt:list[list[str]] = []
        self._ans:list[str] = []
    
    def read_inpt(self) -> None:
        """ Reads in input from user/kattis for the Main and MixedFractions classes to use to solve the problem - stores data in a list
        [[x, x], [x, x], ...] format
        """
        for line in stdin:
            self._inpt.append(line.rstrip().split())

    @property
    def answer(self) -> str:
        """ answer property to handle formatting of self._ans to be printed out later by print_answer() method

        Returns:
            str: Returns formatted string of all the answers returned from MixedFractions.find_mixFrac() method
        """
        return "\n".join([str(t) for t in self._ans])

    def solve(self) -> None:
        """ Method to use _inpt and the find_mixFrac method to find the answer to the kattis problem. The function also appends the 
        answer to the self._ans list for later use
        """
        for frac in self._inpt:
            # print(frac, frac[0],frac[1])
            mixedFxn = MixedFractions(int(frac[0]), int(frac[1]))
            self._ans.append(str(mixedFxn.find_mixFrac()))
        self._ans.append("")

    def print_answer(self) -> None:
        """ This is a method used to write the answers to the console from the self._ans list
        """
        sys.stdout.write(str(self.answer))

    @staticmethod
    def main() -> None:
        """ Method used to handle the Main class and run all the methods
        """
        solution = Main()
        solution.read_inpt()
        solution.solve()
        solution.print_answer()

if __name__ == "__main__":
    Main.main()