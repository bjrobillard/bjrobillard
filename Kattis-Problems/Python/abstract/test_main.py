from __future__ import annotations

__author__ = "Benjamin Robillard"
__class__ = "CSCI 375 - 001"
__assignment__ = "A7 Kattis Problem using ABC"

import sys
import unittest
from unittest.mock import patch
from io import StringIO
from main import Main

class TestMain(unittest.TestCase):
    """ Unittesting Main Class
    """
    @patch('sys.stdout', new_callable=StringIO)
    def test_data(self, mock_stdout:StringIO):
        """ Test data fxn from Main class that returns data gotten from input file or stdin

        Args:
            mock_stdout (StringIO): string description of the cups given from inpt
        """
        data = '3\n12 red\ngreen 6\norange 10'
        with patch('sys.stdin', StringIO(data)):
            sol = Main(sys.stdin)
            sol.data()
        self.assertEqual(sol.data(), [['3'], ['12', 'red'], ['green', '6'], ['orange', '10']])
    
    @patch('sys.stdout', new_callable=StringIO)
    def test_solve(self, mock_stdout:StringIO):
        """ Testing Main.solve() fxn and checking that it returns what it is supposed to

        Args:
            mock_stdout (StringIO): string description of what the cups given are
        """
        data1 = '2\n3 pink\n5 tan'
        with patch('sys.stdin', StringIO(data1)):
            sol = Main(sys.stdin)
            sol.solve()
            sol.print_answer()
            expected: str = 'pink\ntan\n'
        self.assertEqual(mock_stdout.getvalue(), expected)

    @patch('sys.stdout', new_callable=StringIO)
    def test_print_ans(self, mock_stdout:StringIO):
        """ Testing Main.print_answer function and checking that it displays what it's supposed
        to and that it is of the right type (str)

        Args:
            mock_stdout (StringIO): String description of the list of cups given are
        """
        data2 = '3\ngreen 3\norange 4\npurple 5'
        with patch('sys.stdin', StringIO(data2)):
            printans = Main(sys.stdin)
            printans.solve()
            printans.print_answer()
            expected: str = 'green\norange\npurple\n'
        self.assertEqual(mock_stdout.getvalue(), expected)
        self.assertIsInstance(mock_stdout.getvalue(), str)