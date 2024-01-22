Module unittesting
==================

Classes
-------

`Palindrome(not_morse: list[str])`
:   Initializing morse code string to empty string: ""

    ### Methods

    `change_to_morse(self, inptPhrase: list[str]) ‑> str`
    :   This is a function that takes in a list of strings (the input phrase split up) 
            and translates it into morse code for Main.solve() to use to determine if the morse code
            is a palindrome or not
        
        Args:
            inptPhrase (list[str]): list of characters from given input
        
        Returns:
            str: string of morse code characters separated by spaces

    `ret_ans_pal(self, input: list[str]) ‑> list[str]`
    :   This is a function that takes in the list of strings representation of the given input phrase (str) and
            finds what it is in morse code and returns result in a new list - this function looks like the solve() function
            from Main but this returns the list for testing purposes
        
        Args:
            input (list[str]): list of strings input - for testing purposes
        
        Returns:
            list[str]: new list of answer gotten from input and finding if phrase is a morse code palindrome