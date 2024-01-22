import unittest
from tileCost import Hypothesis
from hypothesis import given 
import hypothesis.strategies as some

__author__ = "Benjamin Robillard"
__Kattis_Problem__ = "Title Cost Kattis"
__assignment__ = "Assignment 4"
__class__ = "CSCI 375 - 001"

class Testcases(unittest.TestCase):
    @given(some.tuples(some.text(max_size=30), some.floats(min_value=0, max_value=100)))
    def test_tile_cost_type(self, inpt):
        """ Testing with hypothesis to check if Hypothesis.find_cost() returns the correct type (float)

        Args:
            inpt (Hypothesis(cost, title)): input for Hypothesis class is any combo of letters for the title <30 characters
            and any combo of float nums between 0 and 100
        """  
        st = Hypothesis(inpt[1], inpt[0])
        self.assertIsInstance(st.find_cost(), float)

    @given(some.tuples(some.text(max_size=30), some.floats(min_value=50, max_value=100)))
    def test_tile_cost_accuracy_smaller_than(self, y):
        """ Testing with hypothesis to check if Hypothesis.find_cost returns correct ouput; the len of title is
            less than the cost therefore the cost of the title is the length of the title

        Args:
            y (Hypothesis(cost, title)): input for Hypothesis class is any combo of letters for the title <30 characters
    #         and any combo of float nums between 50 and 100 - making the input always output that the cost of the title
              is just the length of the title
        """
        yt = Hypothesis(y[1], y[0])
        self.assertEqual(yt.find_cost() == len(y[0]), len(y[0]) < (y[1]))

    @given(some.tuples(some.text(max_size=30), some.floats(min_value=0, max_value=29)))
    def test_tile_cost_accuracy_bigger_than(self, z):
        """ Testing with hypothesis to check if Hypothesis.find_cost returns correct ouput; the len of title is
            more than the cost therefore the cost of the title is the budget given in the first place

        Args:
            z (Hypothesis(cost, title)): input for Hypothesis class is any combo of letters for the title <30 characters
    #         and any combo of float nums between 0 and 29 - making the input always output that the cost of the title
              is just the given budget from the input
        """
        zt = Hypothesis(z[1], z[0])
        self.assertEqual(zt.find_cost() == z[1], len(z[0]) >= (z[1]))
        

if __name__ == "__main__":
    unittest.main(verbosity=2)