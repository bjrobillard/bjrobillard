Module cup
==========

Classes
-------

`Cup(cup: Tuple[Any, Any] = (None, None))`
:   This class is used to handle the input given from Main class to determine if
    the cup information is correctly given or not in order for Main.solve 
    to use to solve the kattis problem.
    
    Args:
        object: object class
    
    initializing _input for the is_int function 
    
    Args:
        cup (tuple): input of tuple pair of int or str for both elements in tuple. Defaults to (None, None).

    ### Methods

    `is_int(self) ‑> bool`
    :   takes input from self._input and determines if the first element
        in the given tuple is an integer or not
        
        Returns:
            bool: true/false based on if first element is int or str