from __future__ import annotations
#! usr/bin/env python

from tileCost import Hypothesis
import sys

__author__ = "Benjamin Robillard"
__Kattis_Problem__ = "Title Cost Kattis"
__assignment__ = "Assignment 4"
__class__ = "CSCI 375 - 001"

class Main(object):
    """ Main class to handle all methods and attributes to solve the Title cost kattis problem using the Hypothesis class

    Args:
        object: object class
    """
    def __init__(self) -> None:
        """ Initialize self._ans and self._inpt lists for storing input and output of two classes
        """
        self._ans:list[str] = []
        self._inpt:list[str] = []

    def read_input(self) -> None:
        """ Read in data given by user/kattis and storing info in self._input
        """
        self._inpt = input().split(" ")

    @property
    def answer(self) -> str:
        """ Answer property to format and better store answer into self._ans

        Returns:
            str: returns formatted string representation of answer
        """
        return '\n'.join([str(t) for t in self._ans])

    def solve(self) -> None:
        """ Create Hypothesis class obj using inputted information and appending answer from find_cost() method into self._ans list
        """
        find_cost = Hypothesis(float(self._inpt[1]), str(self._inpt[0]))
        self._ans.append(str(find_cost.find_cost()))
        self._ans.append("")

    def print_ans(self) -> None:
        """ Printing out self.answer property for output for kattis
        """
        sys.stdout.write(str(self.answer))

    @staticmethod
    def main() -> None:
        """ main() method of Main class to handle calling all Main methods to read_input, solve the answer, and print_ans of the problem
        """
        sol = Main()
        sol.read_input()
        sol.solve()
        sol.print_ans()

if __name__ == "__main__":
    Main.main()