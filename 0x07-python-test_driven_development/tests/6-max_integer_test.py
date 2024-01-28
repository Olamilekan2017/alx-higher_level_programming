#!/usr/bin/python3
""" Unittests for max_integer. """


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ Define the test for max_integer """

    def test_positive_int(self):
        """ Test for positive integers in the list """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_negative_int(self):
        """ Test for negative integers in the list """
        self.assertEqual(max_integer([-2, -3, -4, -6]), -2)

    def test_positve_negative_int(self):
        """ Test for both positive and negative integers in the list """
        self.assertEqual(max_integer([-2, 2, -4, 4]), 4)

    def test_duplicate_values(self):
        """ Test for duplicate values in the list """
        self.assertEqual(max_integer([1, 2, 3, 3]), 3)

    def test_empty(self):
        """ Test if the list is empty """
        self.assertEqual(max_integer([]), None)

    def test_one_element(self):
        """ Test if the list contain just one element """
        self.assertEqual(max_integer([7]), 7)

    def test_floats(self):
        """ Test if the list contain float values """
        self.assertEqual(max_integer([2.1, 2.2, 3.1, 6.2]), 6.2)

    def test_int_floats(self):
        """ Test if the list conbtains both int and float values """
        self.assertEqual(max_integer([1, 2.3, 9, 8.2]), 9)

    def test_strings(self):
        """ Test if the list contain strings """
        self.assertEqual(max_integer(["Olayinka", "is", "my", "name"]), "name")


if __name__ == '__main__':
    unittest.main()
