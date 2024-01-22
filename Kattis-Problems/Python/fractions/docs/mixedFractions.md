Module mixedFractions
=====================

Classes
-------

`MixedFractions(numerator: int, denominator: int)`
:   Initializer used to initialize the numerator and denominator attributes of the input given
    
    Args:
        numerator (int): numerator given from the input (number from 1 - ((2^31)-1))
        denominator (int): denominator given from the input (number from 1 - ((2^31)-1))

    ### Methods

    `find_mixFrac(self) ‑> str`
    :   Method used to find and format the mixed fraction gotten from the input from Main class. Returns the mixed fraction
        in the format; {} {} / {}
        
        Returns:
            str: Formatted mixed fraction from the given numerator / denominator