from __future__ import annotations

__author__ = "Benjamin Robillard"
__class__ = "CSCI 375 - 001"
__assignment__ = "A7 Kattis Problem using ABC"

from typing import Any, Tuple
from abc import ABC, abstractmethod
from collections.abc import MutableSequence

from typing import Any, Tuple

class Cup(MutableSequence[int]):
    """ This class is used to handle the input given from Main class to determine if
    the cup information is correctly given or not in order for Main.solve 
    to use to solve the kattis problem.

    Tried to derrive this class from abc.MutableSequence but kept getting errors when it came to doing the type checking... still gives correct ans though

    Args:
        object: object class
    """
    def __init__(self, cup: Tuple[Any, Any] = (None, None)) -> None:
        """ initializing _input for the is_int function 

        Args:
            cup (tuple): input of tuple pair of int or str for both elements in tuple. Defaults to (None, None).
        """
        self._input: Tuple[Any, Any] = cup
        
    def is_int(self) -> bool:
        """ takes input from self._input and determines if the first element
        in the given tuple is an integer or not

        Returns:
            bool: true/false based on if first element is int or str
        """
        try:
            i = int(self._input[0])
        except ValueError:
            return False
        return True

    def __str__(self) -> str:
        """ function to return self._input in human readable form

        Returns:
            str: str representation of self._input (human readable)
        """
        return f"Cup data: {self._input}"

    def __repr__(self) -> str:
        """ function to return self._input in machine readable form

        Returns:
            str: return str representation in machine readable form
        """
        return self.__str__()
    
    def __getitem__(self, index: int) -> Any:
        return self._input[index]

    def __setitem__(self, index: int, value: Any) -> None:
        self._input[index] = value

    def __delitem__(self, index: int) -> None:
        del self._input[index]

    def __len__(self) -> int:
        return len(self._input)

    def insert(self, index: int, value: Any) -> None:
        self._input.insert(index, value)


# class Cup(MutableSequence[int]):
#     """ This class is used to handle the input given from Main class to determine if
#     the cup information is correctly given or not in order for Main.solve 
#     to use to solve the kattis problem.

#     Args:
#         MutableSequence: abstract base class for sequences that can be modified
#     """
#     def __init__(self, cup: Any = [Any, Any]) -> None:
#         """ initializing _input for the is_int function 

#         Args:
#             cup (list, str or int, str or int): input of list pair of int or str for both elements in list. Defaults to [Any, Any].
#         """
#         self._input:tuple[Any, Any] = cup
        
#     def is_int(self) -> bool:
#         """ takes input from self._input and determines if the first element
#         in the given list is an integer or not

#         Returns:
#             bool: true/false based on if first element is int or str
#         """
#         try:
#             i = int(self._input[0])
#         except:
#             return False
#         return True

#     def __str__(self) -> str:
#         """ function to return self._input in human readable form

#         Returns:
#             str: str representation of self._input (human readable)
#         """
#         return f"Cup data: {self._input}"

#     def __repr__(self) -> str:
#         """ function to return self._input in machine readable form

#         Returns:
#             str: return str representation in machine readable form
#         """
#         return self.__str__()

#     def __getitem__(self, index: int) -> Any:
#         return self._input[index]

#     def __setitem__(self, index: int, value: Any) -> None:
#         self._input[index] = value

#     def __delitem__(self, index: int) -> None:
#         del self._input[index]

#     def __len__(self) -> int:
#         return len(self._input)

#     def insert(self, index: int, value: Any) -> None:
#         self._input.insert(index, value)

# class Cup(object):
#     """ This class is used to handle the input given from Main class to determine if
#     the cup information is correctly given or not in order for Main.solve 
#     to use to solve the kattis problem.

#     Args:
#         object: object class
#     """
#     def __init__(self, cup: Any = [Any, Any]) -> None:
#         """ initializing _input for the is_int function 

#         Args:
#             cup (list, str or int, str or int): input of list pair of int or str for both elements in list. Defaults to [Any, Any].
#         """
#         self._input:tuple[Any, Any] = cup
        
#     def is_int(self) -> bool:
#         """ takes input from self._input and determines if the first element
#         in the given list is an integer or not

#         Returns:
#             bool: true/false based on if first element is int or str
#         """
#         try:
#             i = int(self._input[0])
#         except:
#             return False
#         return True

#     def __str__(self) -> str:
#         """ function to return self._input in human readable form

#         Returns:
#             str: str representation of self._input (human readable)
#         """
#         return f"Cup data: {self._input}"

#     def __repr__(self) -> str:
#         """ function to return self._input in machine readable form

#         Returns:
#             str: return str representation in machine readable form
#         """
#         return self.__str__()