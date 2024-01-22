import unittest
from unittest.mock import patch, Mock
from main import Main
from io import StringIO

__author__ = "Benjamin Robillard"
__Kattis_Problem__ = "Statistics Kattis"
__assignment__ = "Assignment 6"
__class__ = "CSCI 375 - 001"

class TestMain(unittest.TestCase):
    @patch('builtins.input', side_effect=['10', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
    def test_solve(self, mock_input):
        """ Test function to test solve function from Main is formatted in the right way after finding the range min and max

        Args:
            mock_input (list[str]): list of numbers for the solve function to run off of
        """
        main = Main()
        main._inpt = [['10', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']]
        main.solve()
        self.assertEqual(main.answer, 'Case 1: 0 9 9\n')

    @patch('sys.stdout', new_callable=Mock)
    def test_print_ans(self, mock_stdout):
        """ Testing that the print_ans function from Main and that it's outputting the correct format

        Args:
            mock_stdout (Mock): Mock object for the print_ans function to test against
        """
        main = Main()
        # self._inpt = [5 0 2 4 6 8]
        main._ans = ['0 8 8']
        main.print_ans()
        mock_stdout.write.assert_called_once_with('0 8 8')


