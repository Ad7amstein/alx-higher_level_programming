#!/usr/bin/python3
"""Defines Unittest for square module."""

import unittest
import pycodestyle
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test suits for square module functiosn."""

    def setUp(self):
        """Executes before any test."""
        Base._Base__nb_objects = 0

    def test_shebang(self):
        """Test shebang."""
        with open('models/square.py', 'r') as file:
            line = file.readline()
            self.assertMultiLineEqual(line, '#!/usr/bin/python3\n')

    def test_pycodestyle(self):
        """Test that we conform to PEP-8."""
        style = pycodestyle.StyleGuide(quit=True)
        result = style.check_files(['models/square.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_function_existence(self):
        """Test function existence"""
        self.assertTrue(hasattr(Square, "__init__"))
        self.assertTrue(hasattr(Square, "__str__"))
        self.assertTrue(hasattr(Square, "update"))
        self.assertTrue(hasattr(Square, "to_dictionary"))

    def test_attributes_existence(self):
        """Test attributes existence"""
        s1 = Square(4)
        self.assertTrue(hasattr(s1, "id"))
        self.assertTrue(hasattr(s1, "size"))
        self.assertTrue(hasattr(s1, "width"))
        self.assertTrue(hasattr(s1, "height"))
        self.assertTrue(hasattr(s1, "x"))
        self.assertTrue(hasattr(s1, "y"))

    def test_docstring(self):
        """Test the documentation of modules and function."""
        self.assertIsNotNone(Square.__doc__)
        self.assertIsNotNone(Square.__init__.__doc__)
        self.assertIsNotNone(Square.__str__.__doc__)
        self.assertIsNotNone(Square.update.__doc__)
        self.assertIsNotNone(Square.to_dictionary.__doc__)

    def test_size(self):
        """Test size attribute."""
        s1 = Square(4)
        self.assertEqual(s1.size, 4)
        self.assertEqual(s1.width, 4)
        self.assertEqual(s1.height, 4)
        self.assertRaises(TypeError, Square, 'size')
        self.assertRaises(TypeError, Square, [1])
        self.assertRaises(ValueError, Square, 0)
        self.assertRaises(ValueError, Square, -3)

    def test_x_y(self):
        s1 = Square(4)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)
        s1.x = 5
        s1.y = 10
        self.assertEqual(s1.x, 5)
        self.assertEqual(s1.y, 10)
        s2 = Square(4, 2, 3)
        self.assertEqual(s2.x, 2)
        self.assertEqual(s2.y, 3)
        self.assertRaises(TypeError, Square, 1, 'x', 5)
        self.assertRaises(TypeError, Square, 1, 6, 'y')
        self.assertRaises(ValueError, Square, 3, -4)
        self.assertRaises(ValueError, Square, 3, 4, -4)

    def test_str(self):
        """Test str method."""
        s1 = Square(5)
        self.assertMultiLineEqual(s1.__str__(), '[Square] '
                                  '(1) 0/0 - 5')

    def test_update(self):
        """Test the update method."""
        s1 = Square(5)
        self.assertMultiLineEqual(s1.__str__(), '[Square] '
                                  '(1) 0/0 - 5')
        s1.update(size=7, y=1)
        self.assertMultiLineEqual(s1.__str__(), '[Square] '
                                  '(1) 0/1 - 7')

        s1.update(size=7, id=89, y=1)
        self.assertMultiLineEqual(s1.__str__(), '[Square] '
                                  '(89) 0/1 - 7')


    def test_to_dictionary(self):
        """Test to dictionary method."""
        s1 = Square(10, 2, 1)
        self.assertMultiLineEqual(s1.__str__(), '[Square] '
                                  '(1) 2/1 - 10')
        s1_dictionary = s1.to_dictionary()
        self.assertIsInstance(s1_dictionary, dict)
        self.assertEqual(s1_dictionary, {
            "id": 1,
            "size": 10,
            "x": 2,
            "y": 1,
        })
        s2 = Square(1, 1)
        self.assertMultiLineEqual(s2.__str__(), '[Square] '
                                  '(2) 1/0 - 1')
        s2.update(**s1_dictionary)
        self.assertMultiLineEqual(s2.__str__(), '[Square] '
                                  '(1) 2/1 - 10')
        self.assertIsNot(s1, s2)
