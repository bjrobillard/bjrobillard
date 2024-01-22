from __future__ import annotations
#! /usr/bin/env python3

__author__ = "Benjamin Robillard"
__Kattis_Problem__ = "Morse Code Palindromes"
__assignment__ = "Assignment 3"
__class__ = "CSCI 375 - 001"

MORSE_CODE_DICT = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 
                   'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---', 
                   'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 
                   'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 
                   'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--', 
                   'z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', 
                   '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----'} # setting the Morse Code Dictionary

class Palindrome(object):
    def __init__(self, not_morse:list[str]) -> None:
        """ Initializing morse code string to empty string: ""
        """
        self._not_morse:list[str] = not_morse
        self._morsecode:str = ""

    def change_to_morse(self, inptPhrase: list[str]) -> str:
        """ This is a function that takes in a list of strings (the input phrase split up) 
            and translates it into morse code for Main.solve() to use to determine if the morse code
            is a palindrome or not

        Args:
            inptPhrase (list[str]): list of characters from given input

        Returns:
            str: string of morse code characters separated by spaces
        """
        word:str = "" 
        # self._morsecode:str = ""
        for char in inptPhrase:
            if char.isalnum():
                word += char.lower()
            elif word:
                if self._morsecode:
                    self._morsecode += " "
                for letter in word:
                    self._morsecode += MORSE_CODE_DICT[letter] + " "
                word = ""
        if word:
            if self._morsecode:
                self._morsecode += " "
            for letter in word:
                self._morsecode += MORSE_CODE_DICT[letter] + " "
        # print(self._morsecode.rstrip())
        return self._morsecode.rstrip()

    def ret_ans_pal(self, input:list[str]) -> list[str]:
        """ This is a function that takes in the list of strings representation of the given input phrase (str) and
            finds what it is in morse code and returns result in a new list - this function looks like the solve() function
            from Main but this returns the list for testing purposes

        Args:
            input (list[str]): list of strings input - for testing purposes

        Returns:
            list[str]: new list of answer gotten from input and finding if phrase is a morse code palindrome
        """
        self._ans = []
        morse_Code = Palindrome(input)
        morsephrase = morse_Code.change_to_morse(input)
        split_morse_phrase = list(morsephrase.replace(" ", ""))    
        if split_morse_phrase: # if listphrase is filled    
            if (split_morse_phrase == split_morse_phrase[::-1]):
                self._ans.append("1")
            else:
                self._ans.append("0")
        else: # if the morse code translation of the input list is empty - print 0
            self._ans.append("0")
        self._ans.append("")

        return self._ans

    def __str__(self) -> str:
        """ Returns string representation of object self._morsecode (human readable)

        Returns:
            str: string representation
        """
        return self._morsecode

    def __repr__(self) -> str:
        """ Returns string representation of object self._morsecode (machine readable)

        Returns:
            str: string representation
        """
        return self.__str__()
