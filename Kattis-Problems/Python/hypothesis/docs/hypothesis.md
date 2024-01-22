Module hypothesis
=================

Classes
-------

`Hypothesis(cost: float, title: str)`
:   This is an class to handle initializing the title and title cost as well as using the find_cost() method to find the cost of the 
        title if it is less than the given budget
    
    Args:
        object: object class
    
    Initialize the title and title cost for the find_cost function
    
    Args:
        cost (float): self._cost of the title given from input() and read_data() methods in Main class
        title (str): self._title of the given input - used to find if budget is surpassed or not

    ### Methods

    `find_cost(self) ‑> float`
    :   Method used to determine if self._title is longer than budget or not
        
        Returns:
            float: returns self._title (length) if length is less than the budget given; returns self._cost if title length
                is smaller than the budget