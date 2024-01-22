import unittest
from main import Main
from unittesting import Palindrome

class TestPalinValues(unittest.TestCase):
    def setUp(self) -> None:
        print("..Set Up..")
        self.main = Main()
        # self.unittesting = Palindrome("")
        self.morse = Palindrome('ACETAT')
        return super().setUp()

    def tearDown(self) -> None:
        print("..Tear Down..")
        return super().tearDown()

    def test_morse_outcome(self):
        """ Testing correctness of change_to_morse() function changing list[str] into morse code string
        """
        Palindrome.change_to_morse(self.morse, ['A', 'C', 'E', 'T', 'A', 'T'])
        morse_list = str(self.morse).rstrip()
        self.assertEqual(morse_list, ".- -.-. . - .- -")

    def test_1st_morse_outcome(self):
        """ Testing correctness of change_to_morse() function changing list[str] into morse code string
        """
        Palindrome.change_to_morse(self.morse, ['T', 'A', 'I', 'N', 'T'])
        morse_list = str(self.morse).rstrip()
        self.assertEqual(morse_list, "- .- .. -. -")

    def test_2nd_morse_outcome(self):
        """ Testing correctness of change_to_morse() function changing list[str] into morse code string
        """
        Palindrome.change_to_morse(self.morse, ['T', 'A', 'I', 'N', 'T']) # I know this is weird but it is a morse code palindrome
        morse_list = str(self.morse).rstrip()
        self.assertNotEqual(morse_list, ".- -.-. . - .- - .-- .")

class TestValues(unittest.TestCase):
    def setUp(self) -> None:
        """ Prints "Set Up" for startUp/TearDown functions after each test
        Returns:
            _type_: prints "Set Up" before test function
        """
        print("Set Up")
        self.main = Main()
        self.morse = Palindrome('ACETAT')
        self.diff_morse = Palindrome('ACETATE')
        return super().setUp()

    def tearDown(self) -> None:
        """ Prints "Tear Down" for startUp/TearDown functions after each test

        Returns:
            _type_: prints "Tear Down" after test function
        """
        print("Tear Down")
        return super().tearDown()

    # Tests for Main input methods
    def test_valid_input(self):
        self.assertEqual(type(self.main.data()), str)

    def test_another_valid_input(self):
        """ Test a valid input for input
        """
        self.assertEqual(type("POOP"), type(self.main.data()))
    
    def test_invalid_input(self):
        """ Testing invalid type (not string is what data() returns)
        """
        self.assertNotEqual(type(self.main.data()), 123)
    

    # Test correct solve outputs from ret_ans() for solve which uses change_to_morse()
    def test_incorrect_solve(self):
        """ check that the return answer for [.- -.-. . - .- -] returns '0'
        """
        self.main.solve()
        self.assertEqual(self.main.ret_ans(), ['0',''])

    def test_correct_solve(self):
        """ check that the return answer for [.- -.-. . - .- -] returns '0'
        """
        self.main = Main()
        self.assertEqual(self.morse.ret_ans_pal("ACETATE"), ['1',''])

    def test_another_correct_solve(self):
        """ check that the return answer for [.- -.-. . - .- -] returns '1'
        """
        self.main = Main()
        self.assertEqual(self.morse.ret_ans_pal("TAINT"), ['1',''])