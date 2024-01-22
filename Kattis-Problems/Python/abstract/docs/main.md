Module main
===========

Classes
-------

`Main(data_source: Any = sys.stdin)`
:   This class is used to handle the reading of input given from kattis/user
    input and solving the kattis problem (stacking cups). It formats the answer
    and prints it to the console for kattis to check the solution.
    
    Args:
            Kattis: Kattis abstract based class
    
    initializing Main class to handle reading input, solving the problem, formatting and printing the answer
    
    Args:
            data_source (Any, optional): reading input from sys.stdin from user. Defaults to sys.stdin.

    ### Ancestors (in MRO)

    * kattis.Kattis
    * abc.ABC

    ### Instance variables

    `answer: Any`
    :   Formatting _answer so that kattis will accept the answer
        
        Returns:
                Any: formatted answer gotten from Main.solve

    ### Methods

    `data(self) ‑> Any`
    :   Data method to return the data given from user or data file 
        
        Returns:
                Any: list[[int or str, int or str], [int or str, int or str], ...]

    `print_answer(self) ‑> None`
    :   Printing answer to console

    `read_input(self) ‑> None`
    :   Reading input given from data file or user input

    `solve(self) ‑> None`
    :   Solve method used to find answer gotten from Cup.is_int() and uses what it 
        returns to know what to append to sorted_cups. sorted_cups is then sorted and assigned to 
        _answer attribute for later use