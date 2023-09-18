#!/usr/bin/python3
"""Defines Unittest for rectangle module."""

import unittest
import pycodestyle
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestRectangle(unittest.TestCase):
    """Test suits for rectangle module functiosn."""

    def setUp(self):
        """Executes before any test."""
        Base._Base__nb_objects = 0

    def test_shebang(self):
        """Test shebang."""
        with open('models/rectangle.py', 'r') as file:
            line = file.readline()
            self.assertMultiLineEqual(line, '#!/usr/bin/python3\n')

    def test_pycodestyle(self):
        """Test that we conform to PEP-8."""
        style = pycodestyle.StyleGuide(quit=True)
        result = style.check_files(['models/rectangle.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_function_existence(self):
        """Test function existence"""
        self.assertTrue(hasattr(Rectangle, "__init__"))
        self.assertTrue(hasattr(Rectangle, "__str__"))
        self.assertTrue(hasattr(Rectangle, "update"))
        self.assertTrue(hasattr(Rectangle, "area"))
        self.assertTrue(hasattr(Rectangle, "display"))
        self.assertTrue(hasattr(Rectangle, "to_dictionary"))

    def test_attributes_existence(self):
        """Test attributes existence"""
        s1 = Square(4)
        self.assertTrue(hasattr(s1, "id"))
        self.assertTrue(hasattr(s1, "width"))
        self.assertTrue(hasattr(s1, "height"))
        self.assertTrue(hasattr(s1, "x"))
        self.assertTrue(hasattr(s1, "y"))

    def test_docstring(self):
        """Test the documentation of modules and function."""
        self.assertIsNotNone(Rectangle.__doc__)
        self.assertIsNotNone(Rectangle.__init__.__doc__)
        self.assertIsNotNone(Rectangle.__str__.__doc__)
        self.assertIsNotNone(Rectangle.update.__doc__)
        self.assertIsNotNone(Rectangle.to_dictionary.__doc__)
        self.assertIsNotNone(Rectangle.area.__doc__)
        self.assertIsNotNone(Rectangle.display.__doc__)

    def test_width_height(self):
        """Test width attribute."""
        r1 = Rectangle(4, 5)
        self.assertEqual(r1.width, 4)
        self.assertEqual(r1.height, 5)
        self.assertRaises(TypeError, Rectangle, 'size', 5)
        self.assertRaises(TypeError, Rectangle, 5, 'size')
        self.assertRaises(TypeError, Rectangle, [1])
        self.assertRaises(ValueError, Rectangle, 0, 3)
        self.assertRaises(ValueError, Rectangle, 2, 0)
        self.assertRaises(ValueError, Rectangle, -3, 4)
        self.assertRaises(ValueError, Rectangle, 3, -2)

    def test_x_y(self):
        r1 = Rectangle(4, 5)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        r1.x = 5
        r1.y = 10
        self.assertEqual(r1.x, 5)
        self.assertEqual(r1.y, 10)
        r2 = Rectangle(4, 10, 2, 3)
        self.assertEqual(r2.x, 2)
        self.assertEqual(r2.y, 3)
        self.assertRaises(TypeError, Rectangle, 1, 2, 'x', 5)
        self.assertRaises(TypeError, Rectangle, 1, 2, 6, 'y')
        self.assertRaises(ValueError, Rectangle, 3, 2, -4)
        self.assertRaises(ValueError, Rectangle, 3, 2, 4, -4)

    def test_str(self):
        """Test str method."""
        r1 = Rectangle(4, 5)
        self.assertMultiLineEqual(r1.__str__(), '[Rectangle] '
                                  '(1) 0/0 - 4/5')

    def test_update1(self):
        """Test the update method."""
        r1 = Rectangle(10, 10, 10, 10)
        self.assertMultiLineEqual(
            r1.__str__(), '[Rectangle] (1) 10/10 - 10/10')

        r1.update(89)
        self.assertMultiLineEqual(
            r1.__str__(), '[Rectangle] (89) 10/10 - 10/10')

        r1.update(89, 2)
        self.assertMultiLineEqual(
            r1.__str__(), '[Rectangle] (89) 10/10 - 2/10')

        r1.update(89, 2, 3)
        self.assertMultiLineEqual(r1.__str__(), '[Rectangle] (89) 10/10 - 2/3')

        r1.update(89, 2, 3, 4)
        self.assertMultiLineEqual(r1.__str__(), '[Rectangle] (89) 4/10 - 2/3')

        r1.update(89, 2, 3, 4, 5)
        self.assertMultiLineEqual(r1.__str__(), '[Rectangle] (89) 4/5 - 2/3')

    def test_update2(self):
        """Test the update method."""
        r1 = Rectangle(10, 10, 10, 10)
        self.assertMultiLineEqual(
            r1.__str__(), '[Rectangle] (1) 10/10 - 10/10')

        r1.update(height=1)
        self.assertMultiLineEqual(r1.__str__(), '[Rectangle] (1) 10/10 - 10/1')

        r1.update(width=1, x=2)
        self.assertMultiLineEqual(r1.__str__(), '[Rectangle] (1) 2/10 - 1/1')

        r1.update(y=1, width=2, x=3, id=89)
        self.assertMultiLineEqual(r1.__str__(), '[Rectangle] (89) 3/1 - 2/1')

        r1.update(x=1, height=2, y=3, width=4)
        self.assertMultiLineEqual(r1.__str__(), '[Rectangle] (89) 1/3 - 4/2')

    def test_to_dictionary(self):
        """Test to dictionary method."""
        r1 = Rectangle(10, 2, 1, 9)
        self.assertMultiLineEqual(r1.__str__(), '[Rectangle] (1) 1/9 - 10/2')
        r1_dictionary = r1.to_dictionary()
        self.assertIsInstance(r1_dictionary, dict)
        self.assertEqual(r1_dictionary, {
            'id': 1, 'width': 10, 'height': 2, 'x': 1, 'y': 9})

        r2 = Rectangle(1, 1)
        self.assertMultiLineEqual(r2.__str__(), '[Rectangle] (2) 0/0 - 1/1')
        r2.update(**r1_dictionary)
        self.assertMultiLineEqual(r2.__str__(), '[Rectangle] (1) 1/9 - 10/2')
        self.assertIsNot(r1, r2)

    def test_area(self):
        """Test area method."""
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.area(), 20)

        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 56)
