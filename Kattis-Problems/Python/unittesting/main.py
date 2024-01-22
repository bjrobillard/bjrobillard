from __future__ import annotations
#! /usr/bin/env python3

__author__ = "Benjamin Robillard"
__Kattis_Problem__ = "Morse Code Palindromes"
__assignment__ = "Assignment 3"
__class__ = "CSCI 375 - 001"

from unittesting import Palindrome
import sys
# import unittest

class Main(object):
    def __init__(self) -> None:
        """ Initialize _phrase and _ans for solving kattis problem
        """
        self._phrase:str = ""
        self._ans:list[str] = []
    
    def read_in_data(self) -> None:
        """ Reading in data from user/kattis input
        """
        self._phrase = input()

    def print_data(self) -> None:
        """ Print self._phrase to console (for debugging)
        """
        print(f"The input phrase is: {self._phrase}")

    def data(self) -> str:
        """ Method for returning self._phrase

        Returns:
            str: Phrase brought in from kattis/user
        """
        return self._phrase

    @property
    def answer(self) -> str:
        """ Formatting answer for ouput

        Returns:
            str: Formatted answer from self._ans
        """
        return '\n'.join([str(t) for t in self._ans])


    def solve(self) -> None:
        """ Uses self._phrase to make a Palindrome object to be translated to morse
            code to then be used to find answer
        """
        listphrase = list(self._phrase.replace(" ", ""))
        morse_Code = Palindrome(listphrase)
        morsephrase = morse_Code.change_to_morse(listphrase)
        split_morse_phrase = list(morsephrase.replace(" ", ""))    
        if split_morse_phrase: # if listphrase is filled    
            if (split_morse_phrase == split_morse_phrase[::-1]):
                self._ans.append("1")
            else:
                self._ans.append("0")
        else: # if the morse code translation of the input list is empty - print 0
            self._ans.append("0")

        self._ans.append("")        

    def print_answer(self) -> None:
        """ Print out answer to console using 'answer' property
        """
        # self._ans.append(self.answer)
        sys.stdout.write(str(self.answer))

    def ret_ans(self) -> list[str]:
        """ Return self._ans for Main

        Returns:
            _type_: return self._ans for testing purposes
        """
        return self._ans

    @staticmethod
    def main() -> None:
        """ Main static method to create Main object and call in 
            read_in_data(), solve(), print_answer() methods
        """
        sol = Main()
        sol.read_in_data()
        sol.solve()
        sol.print_answer()

    def __str__(self) -> str: 
        """ Returns HR form of self._ans (the answers from solve())

        Returns:
            _type_: string representation of self._ans gotten from solve() and change_to_morse()
        """
        return str(self._ans)

if __name__ == "__main__":
    Main.main()
