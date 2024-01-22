from __future__ import annotations

#! /usr/bin/env python

__author__ = "Benjamin Robillard"
__Kattis_Problem__ = "Statistics Kattis"
__assignment__ = "Assignment 6"
__class__ = "CSCI 375 - 001"

import sys
from stats import Statistics

class Main(object):
    def __init__(self) -> None:
        """ Initialize self._input list to store the input from kattis/user and self._ans to store the answer string
        """
        self._inpt:list[list[str]] = []
        self._ans:list[str] = []

    def read_in_data(self) -> None:
        """ Reading in data from kattis/user and putting each line into tuple for Main.solve() to use
        """
        for line in sys.stdin.readlines():
            self._inpt.append(line.split())
        #     print(line)
        # print(self._inpt)

    @property
    def answer(self) -> str:
        """ Format self._ans for print_ans() to print out to console

        Returns:
            str: Formatted string representation of self._ans and all that is contained in the list
        """
        return '\n'.join([str(t) for t in self._ans])

    def solve(self) -> None:
        """ Append answer from Statistics.find_stats() to self._ans to use later. Also formats correct output for kattis 
            to test against (i.e Case X: X X X)
        """
        i = 1
        for line in self._inpt:
            stats = Statistics([int(t) for t in line])
            self._ans.append("Case " + str(i) + ": " + stats.find_stats())
            i += 1
        self._ans.append("")

    def print_ans(self) -> None:
        """ Print out answer from Main.answer property (after being formatted correctly)
        """
        sys.stdout.write(str(self.answer))

    @staticmethod
    def main() -> None:
        """ main method to run the other methods of Main class
        """
        sol = Main()
        sol.read_in_data()
        sol.solve()
        sol.print_ans()

if __name__ == "__main__":
    Main.main()

