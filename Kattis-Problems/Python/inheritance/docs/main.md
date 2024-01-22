Module main
===========

Classes
-------

`Main()`
:   Initialize self._input list to store the input from kattis/user and self._ans to store the answer string

    ### Static methods

    `main() ‑> None`
    :   main method to run the other methods of Main class

    ### Instance variables

    `answer: str`
    :   Format self._ans for print_ans() to print out to console
        
        Returns:
            str: Formatted string representation of self._ans and all that is contained in the list

    ### Methods

    `print_ans(self) ‑> None`
    :   Print out answer from Main.answer property (after being formatted correctly)

    `read_in_data(self) ‑> None`
    :   Reading in data from kattis/user and putting each line into tuple for Main.solve() to use

    `solve(self) ‑> None`
    :   Append answer from Statistics.find_stats() to self._ans to use later. Also formats correct output for kattis 
        to test against (i.e Case X: X X X)