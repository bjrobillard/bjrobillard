import unittest
from unittest.mock import patch, Mock
from main import Main
from io import StringIO

__author__ = "Benjamin Robillard"
__Kattis_Problem__ = "Title Cost Kattis"
__assignment__ = "Assignment 4"
__class__ = "CSCI 375 - 001"

class TestMain(unittest.TestCase):
    @patch('builtins.input', side_effect=['red 10.0'])
    def test_solve(self, mock_input):
        """ Mock and Patch test function to check that the Main.solve method is working correctly - 
        it makes a Main object and reads in the given data: red 10.0, and uses the solve method to solve
        it and then tests that the main.answer string correctly outputs 3.0

        Args:
            mock_input (list[str]): list element of 'red 10.0' 
        """
        main = Main()
        main.read_input()
        main.solve()
        self.assertEqual(main.answer, '3.0\n')

    @patch('builtins.input', side_effect=['green 5.0'])
    def test_solve_1(self, mock_input):
        """ Mock and Patch test function to check that the Main.solve method is working correctly - 
        it makes a Main object and reads in the given data: green 5.0, and uses the solve method to solve
        it and then tests that the main.answer string correctly outputs 5.0 

        Args:
            mock_input (list[str]): list element of 'green 5.0'
        """
        main = Main()
        main.read_input()
        main.solve()
        self.assertEqual(main.answer, '5.0\n')

    def test_print_ans(self):
        """ Test function to make sure main._ans is correctly printed out using Main.print_ans method in the format of
        'float\nfloat\nfloat\n depending on what Main.solve gets as an output after formatting - in the kattis scenario 
        there is no input data that consists of more than one input, this was just for the sake of testing the formatted output
        """
        main = Main()
        main._ans = ['100.0', '200.0', '150.0', '']
        expected_output = '100.0\n200.0\n150.0\n'
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            main.print_ans()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=Mock)
    def test_print_ans(self, mock_stdout):
        """ Mock and Patch test function that uses the sys.stdout method and xxx.write.assert_called_once_with to test that 
        with the given main._ans list, it outputs the answer only once

        Args:
            mock_stdout (Mock callable): Mock callable to use for the sys.stdout portion of this method
        """
        main = Main()
        main._ans = ['200.000000', '']
        main.print_ans()
        mock_stdout.write.assert_called_once_with('200.000000\n')

if __name__ == "__main__":
    unittest.main(verbosity=2)