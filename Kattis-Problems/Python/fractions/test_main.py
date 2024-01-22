from __future__ import annotations

__author__ = "Benjamin Robillard"
__Kattis_Problem__ = "Mixed Fractions Kattis"
__assignment__ = "Assignment 5"
__class__ = "CSCI 375 - 001"

import unittest 
from unittest.mock import patch, Mock
from main import Main
from io import StringIO

class TestMain(unittest.TestCase):
    @patch('builtins.input', side_effect=['10', '20'])
    def test_solve(self, mock_input):
        """ Testing Main.solve() method and makes sure that it returns the correct output using the unittest Mock/Patch 
        tool to test with stdin and stdout used by Main

        Args:
            mock_input (list[str]): an example tuple for the test method to test with
        """
        main = Main()
        main._inpt = [['10', '20']]
        # main.read_inpt()
        main.solve()
        self.assertEqual(main.answer, '0 10 / 20\n')
    
    @patch('sys.stdout', new_callable=Mock)
    def test_print_ans(self, mock_stdout):
        """ Testing Main.print_answer() to make sure it prints out the correct format of the mixed fraction

        Args:
            mock_stdout (Mock): Mock input for test_print_ans to test with
        """
        main = Main()
        main._ans = ['2 0 / 100']
        main.print_answer()
        mock_stdout.write.assert_called_once_with('2 0 / 100')

if __name__ == "__main__":
    unittest.main(verbosity=2)