Module main
===========

Classes
-------

`Main()`
:   Main class to handle all methods and attributes to solve the Title cost kattis problem using the Hypothesis class
    
    Args:
        object: object class
    
    Initialize self._ans and self._inpt lists for storing input and output of two classes

    ### Static methods

    `main() ‑> None`
    :   main() method of Main class to handle calling all Main methods to read_input, solve the answer, and print_ans of the problem

    ### Instance variables

    `answer: str`
    :   Answer property to format and better store answer into self._ans
        
        Returns:
            str: returns formatted string representation of answer

    ### Methods

    `print_ans(self) ‑> None`
    :   Printing out self.answer property for output for kattis

    `read_input(self) ‑> None`
    :   Read in data given by user/kattis and storing info in self._input

    `solve(self) ‑> None`
    :   Create Hypothesis class obj using inputted information and appending answer from find_cost() method into self._ans list