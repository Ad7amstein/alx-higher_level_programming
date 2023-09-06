#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_integer([..]).
    """

    def test_max_at_beginning(self):
        """Test max at the beginning."""
        self.assertAlmostEqual(max_integer([4, 2, 3, 1]), 4)

    def test_ordered_list(self):
        """Test an ordered list of integers."""
        self.assertAlmostEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test an unordered list of integers."""
        self.assertAlmostEqual(max_integer([2, 3, 4, 1]), 4)

    def test_empty_list(self):
        """Test an empty list."""
        self.assertAlmostEqual(max_integer([]), None)

    def test_negative_values(self):
        """Test a list of negative integers."""
        self.assertAlmostEqual(max_integer([-10, -2, -4, -8]), -2)

    def test_one_element_list(self):
        """Test for one element list."""
        self.assertAlmostEqual(max_integer([1]), 1)

    def test_list_of_floats_integers(self):
        """Test a list of floats and integers."""
        self.assertAlmostEqual(max_integer([1.4, 15.9, -12, 11, 10]), 15.9)

    def test_string(self):
        """Test a list of characters."""
        text = "ADHAMZ"
        self.assertAlmostEqual(max_integer(text), 'Z')

    def test_list_strings(self):
        """Test a list of strings."""
        strings = ['Adham', 'hi', 'ZOO']
        self.assertAlmostEqual(max_integer(strings), 'hi')

    def test_empty_string(self):
        """Test empty string."""
        self.assertAlmostEqual(max_integer(""), None)


if __name__ == "__main__":
    unittest.main()
