#! /usr/bin/env python3

"""
unittesting buka solution
"""

__author__ = "Benjamin Robillard"

import unittest
from buka import answer

class TestBuka(unittest.TestCase):
    def test1_answer(self):
        self.assertEqual(answer(10, "*", 10), 100, "wrong")
    
    def test2_answer(self):
        self.assertEqual(answer(100, "+", 100), 200, "wrong")

    def test3_answer(self):
        self.assertEqual(answer(10, "+", 10), 20, "wrong")

    def test4_answer(self):
        self.assertEqual(answer(100, "*", 10), 1000, "wrong")

    def test5_answer(self):
        self.assertEqual(answer(1000, "+", 100), 1100, "wrong")
    
    def test6_answer(self):
        self.assertEqual(answer(1000, "*", 100), 100000, "wrong")


if __name__ == "__main__":
    unittest.main(verbosity=2)


# #! /usr/bin/env python3

# import unittest
# from buka import answer


# # class TestHello(unittest.TestCase):
# #     def test_case1(self):
# #         ans = answer(10, "*", 10)
# #         self.asserEqual(answer())
# #         self.assertEqual(buka.answer() == "hello World")

# def testing_answer():
#     input1 = 10
#     op1 = "+"
#     input1_2 = 10
#     assert answer(input1, op1, input1_2) == 20

#     input2 = 100
#     op2 = "*"
#     input2_2 = 10
#     assert answer(input2, op2, input2_2) == 1000

#     input3 = 30
#     op3 = "*"
#     input3_2 = 20
#     assert answer(input3, op3, input3_2) == 600

#     input4 = 50
#     op4 = "+"
#     input4_2 = 100
#     assert answer(input4, op4, input4_2) == 150

#     input5 = 1000
#     op5 = "*"
#     input5_2 = 10000
#     assert answer(input5, op5, input5_2) == 10000000

#     input6 = 110
#     op6 = "+"
#     input6_2 = 110
#     assert answer(input6, op6, input6_2) == 220

#     print("All test cases passed...")



# # class TestBuka(unittest.TestCase):
# #     def test_case1(self):
# #         self.assertEqual(answer(10, "*", 10) == 100, True, "wrong")
# #     def test_case2(self):
# #         self.assertEqual(answer(10, "+", 10) == 20, True, "wrong")
# #     def test_case3(self):
# #         self.assertEqual(answer(100, "*", 100) == 20000, False, "right")
# #     def test_case4(self):
# #         self.assertEqual(answer(1000, "+", 1000) == 2000, True, "wrong")
# #     def test_case5(self):
# #         self.assertEqual(answer(1000, "+", 1000) == 3000, False, "right")
# #     def test_case6(self):
# #         self.assertEqual(answer(1000, "+", 1000) == 1000, False, "right")    

# # if __name__ == "__main__":
# #     test_answer()


# if __name__ == "__main__":
#     # unittest.main(verbosity=2)
#     testing_answer()
