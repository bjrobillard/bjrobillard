Module stats
============

Classes
-------

`BaseStatistics(inputLine: list[int])`
:   Initialize self._inputLine for BaseStatistics to use as the input data
    
    Args:
        inputLine (list): List of numbers to use to find the min, max, and range

    ### Descendants

    * stats.Statistics

    ### Methods

    `find_max(self) ‑> int`
    :   Method to find max value from the given input data
        
        Returns:
            int: Max value of the input data

    `find_min(self) ‑> int`
    :   Method used to find the min value from the given input data
        
        Returns:
            int: Min value of the input data

`Statistics(inputLine: list[int])`
:   Initialize the Class to use the given input data that BaseStatistics is given
    
    Args:
        inputLine (list): List of numbers

    ### Ancestors (in MRO)

    * stats.BaseStatistics

    ### Methods

    `find_range(self) ‑> int`
    :   Finding range of inputs using the find_min() and find_max() functions from BaseStatistics
        
        Returns:
            int: range from inputs

    `find_stats(self) ‑> str`
    :   Format stats gotten from find_range(), find_min(), and find_max() so that they're in the right
        order and separated by a space.
        
        Returns:
            str: min max range - from inputs given