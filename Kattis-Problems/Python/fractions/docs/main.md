Module main
===========

Classes
-------

`Main()`
:   Initializer for Main class - initializes self._inpt (list to store inputs from user/kattis) and self._ans (list to store
    answers to be written out)

    ### Static methods

    `main() ‑> None`
    :   Method used to handle the Main class and run all the methods

    ### Instance variables

    `answer: str`
    :   answer property to handle formatting of self._ans to be printed out later by print_answer() method
        
        Returns:
            str: Returns formatted string of all the answers returned from MixedFractions.find_mixFrac() method

    ### Methods

    `print_answer(self) ‑> None`
    :   This is a method used to write the answers to the console from the self._ans list

    `read_inpt(self) ‑> None`
    :   Reads in input from user/kattis for the Main and MixedFractions classes to use to solve the problem - stores data in a list
        [[x, x], [x, x], ...] format

    `solve(self) ‑> None`
    :   Method to use _inpt and the find_mixFrac method to find the answer to the kattis problem. The function also appends the 
        answer to the self._ans list for later use