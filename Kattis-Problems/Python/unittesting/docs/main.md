Module main
===========

Classes
-------

`Main()`
:   Initialize _phrase and _ans for solving kattis problem

    ### Static methods

    `main() ‑> None`
    :   Main static method to create Main object and call in 
        read_in_data(), solve(), print_answer() methods

    ### Instance variables

    `answer: str`
    :   Formatting answer for ouput
        
        Returns:
            str: Formatted answer from self._ans

    ### Methods

    `data(self) ‑> str`
    :   Method for returning self._phrase
        
        Returns:
            str: Phrase brought in from kattis/user

    `print_answer(self) ‑> None`
    :   Print out answer to console using 'answer' property

    `print_data(self) ‑> None`
    :   Print self._phrase to console (for debugging)

    `read_in_data(self) ‑> None`
    :   Reading in data from user/kattis input

    `ret_ans(self) ‑> list[str]`
    :   Return self._ans for Main
        
        Returns:
            _type_: return self._ans for testing purposes

    `solve(self) ‑> None`
    :   Uses self._phrase to make a Palindrome object to be translated to morse
        code to then be used to find answer