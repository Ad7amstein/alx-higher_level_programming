#!/usr/bin/python3
"""Defines Unittest for base module."""

import unittest
import pycodestyle
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Test suits for base module functiosn."""

    def setUp(self):
        """Executes before any test."""
        Base._Base__nb_objects = 0

    def test_shebang(self):
        """Test shebang."""
        with open('models/base.py', 'r') as file:
            line = file.readline()
            self.assertMultiLineEqual(line, '#!/usr/bin/python3\n')

    def test_pycodestyle(self):
        """Test that we conform to PEP-8."""
        style = pycodestyle.StyleGuide(quit=True)
        result = style.check_files(['models/base.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_function_existence(self):
        """Test function existence"""
        self.assertTrue(hasattr(Base, "__init__"))
        self.assertTrue(hasattr(Base, "to_json_string"))
        self.assertTrue(hasattr(Base, "save_to_file"))
        self.assertTrue(hasattr(Base, "from_json_string"))
        self.assertTrue(hasattr(Base, "create"))
        self.assertTrue(hasattr(Base, "load_from_file"))
        self.assertTrue(hasattr(Base, "save_to_file_csv"))
        self.assertTrue(hasattr(Base, "load_from_file_csv"))
        self.assertTrue(hasattr(Base, "draw"))

    def test_docstring(self):
        """Test the documentation of modules and function."""
        self.assertIsNotNone(Base.__doc__)
        self.assertIsNotNone(Base.__init__.__doc__)
        self.assertIsNotNone(Base.to_json_string.__doc__)
        self.assertIsNotNone(Base.save_to_file.__doc__)
        self.assertIsNotNone(Base.from_json_string.__doc__)
        self.assertIsNotNone(Base.create.__doc__)
        self.assertIsNotNone(Base.load_from_file.__doc__)
        self.assertIsNotNone(Base.save_to_file_csv.__doc__)
        self.assertIsNotNone(Base.load_from_file_csv.__doc__)
        self.assertIsNotNone(Base.draw.__doc__)

    def test_attributes_existence(self):
        """Test attributes existence"""
        b1 = Base()
        self.assertTrue(hasattr(b1, '_Base__nb_objects'))
        self.assertTrue(hasattr(b1, 'id'))

    def test_id(self):
        """Test id."""
        b1 = Base(-20)
        b2 = Base()
        b3 = Base(18)
        b4 = Base()
        b5 = Base()
        self.assertEqual(b1.id, -20)
        self.assertEqual(b2.id, 1)
        self.assertEqual(b3.id, 18)
        self.assertEqual(b4.id, 2)
        self.assertEqual(b5.id, 3)

    def test_to_json_string(self):
        """Test to json string."""
        self.assertEqual(Base.to_json_string(None), '[]')
        self.assertEqual(Base.to_json_string([]), '[]')
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_string = Base.to_json_string([dictionary])
        self.assertIsInstance(json_string, str)
        self.assertEqual(
            json_string,
            '[{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}]')

    def test_from_json_string(self):
        """Test from json string."""
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string([]), [])
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertIsInstance(list_output, list)
        self.assertEqual(list_output, [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}])
        self.assertEqual(list_output, list_input)
        self.assertIsNot(list_output, list_input)

    def test_save_to_file(self):
        """Test save to file and load from file."""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as file:
            self.assertMultiLineEqual(file.read(),
                                      '[{"id": 1, "width": 10, "height": 7, '
                                      '"x": 2, "y": 8}, '
                                      '{"id": 2, "width": 2, "height": 4, '
                                      '"x": 0, "y": 0}]')

        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), '[]')
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), '[]')

    def test_load_from_file_rectangle(self):
        """Test load from file."""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]

        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        self.assertIsInstance(list_rectangles_output, list)
        self.assertEqual(len(list_rectangles_output), 2)
        for rec in list_rectangles_output:
            self.assertIsInstance(rec, Rectangle)
        self.assertNotEqual(id(list_rectangles_output[0]),
                            id(list_rectangles_output[1]))
        self.assertIsNot(r1, list_rectangles_output[0])
        self.assertIsNot(r2, list_rectangles_output[1])
        self.assertEqual(r1.width, list_rectangles_output[0].width)
        self.assertEqual(r1.height, list_rectangles_output[0].height)
        self.assertEqual(r1.id, list_rectangles_output[0].id)
        self.assertEqual(r1.x, list_rectangles_output[0].x)
        self.assertEqual(r1.y, list_rectangles_output[0].y)
        self.assertEqual(r2.width, list_rectangles_output[1].width)
        self.assertEqual(r2.height, list_rectangles_output[1].height)
        self.assertEqual(r2.id, list_rectangles_output[1].id)
        self.assertEqual(r2.x, list_rectangles_output[1].x)
        self.assertEqual(r2.y, list_rectangles_output[1].y)
        Rectangle.save_to_file(None)
        self.assertEqual(Rectangle.load_from_file(), [])
        Rectangle.save_to_file([])
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_load_from_file_square(self):
        """Test load from file."""
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        list_squares_input = [s1, s2]

        Square.save_to_file(list_squares_input)
        list_squares_output = Square.load_from_file()
        self.assertIsInstance(list_squares_output, list)
        self.assertEqual(len(list_squares_output), 2)
        for sq in list_squares_output:
            self.assertIsInstance(sq, Square)
        self.assertNotEqual(id(list_squares_output[0]),
                            id(list_squares_output[1]))
        self.assertIsNot(s1, list_squares_output[0])
        self.assertIsNot(s2, list_squares_output[1])
        self.assertEqual(s1.id, list_squares_output[0].id)
        self.assertEqual(s1.width, list_squares_output[0].width)
        self.assertEqual(s1.height, list_squares_output[0].height)
        self.assertEqual(s1.x, list_squares_output[0].x)
        self.assertEqual(s1.y, list_squares_output[0].y)
        self.assertEqual(s2.id, list_squares_output[1].id)
        self.assertEqual(s2.width, list_squares_output[1].width)
        self.assertEqual(s2.height, list_squares_output[1].height)
        self.assertEqual(s2.x, list_squares_output[1].x)
        self.assertEqual(s2.y, list_squares_output[1].y)
        Square.save_to_file(None)
        self.assertEqual(Square.load_from_file(), [])
        Square.save_to_file([])
        self.assertEqual(Square.load_from_file(), [])

    def test_create_rectangle(self):
        """Test create method."""
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertIsInstance(r2, Rectangle)
        self.assertEqual(r2.id, r1.id)
        self.assertEqual(r2.width, r1.width)
        self.assertEqual(r2.height, r1.height)
        self.assertEqual(r2.x, r1.x)
        self.assertEqual(r2.y, r1.y)
        self.assertIsNot(r1, r2)
        self.assertNotEqual(r1, r2)

    def test_create_square(self):
        """Test create method."""
        r1 = Square(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Square.create(**r1_dictionary)
        self.assertIsInstance(r2, Square)
        self.assertEqual(r2.id, r1.id)
        self.assertEqual(r2.width, r1.width)
        self.assertEqual(r2.height, r1.height)
        self.assertEqual(r1.size, r2.size)
        self.assertEqual(r2.x, r1.x)
        self.assertEqual(r2.y, r1.y)
        self.assertIsNot(r1, r2)
        self.assertNotEqual(r1, r2)

    def test_csv_file_handlers_rectangle(self):
        """Test save to file csv."""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]

        Rectangle.save_to_file_csv(list_rectangles_input)

        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertIsInstance(list_rectangles_output, list)
        self.assertEqual(len(list_rectangles_output), 2)
        for rec in list_rectangles_output:
            self.assertIsInstance(rec, Rectangle)
        self.assertNotEqual(id(list_rectangles_output[0]),
                            id(list_rectangles_output[1]))
        self.assertIsNot(r1, list_rectangles_output[0])
        self.assertIsNot(r2, list_rectangles_output[1])
        self.assertEqual(r1.width, list_rectangles_output[0].width)
        self.assertEqual(r1.height, list_rectangles_output[0].height)
        self.assertEqual(r1.id, list_rectangles_output[0].id)
        self.assertEqual(r1.x, list_rectangles_output[0].x)
        self.assertEqual(r1.y, list_rectangles_output[0].y)
        self.assertEqual(r2.width, list_rectangles_output[1].width)
        self.assertEqual(r2.height, list_rectangles_output[1].height)
        self.assertEqual(r2.id, list_rectangles_output[1].id)
        self.assertEqual(r2.x, list_rectangles_output[1].x)
        self.assertEqual(r2.y, list_rectangles_output[1].y)
        Rectangle.save_to_file(None)
        self.assertEqual(Rectangle.load_from_file(), [])
        Rectangle.save_to_file([])
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_csv_file_handlers_rectangle(self):
        """Test save to file csv."""
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        list_squares_input = [s1, s2]

        Square.save_to_file_csv(list_squares_input)

        list_squares_output = Square.load_from_file_csv()
        self.assertIsInstance(list_squares_output, list)
        self.assertEqual(len(list_squares_output), 2)
        for sq in list_squares_output:
            self.assertIsInstance(sq, Square)
        self.assertNotEqual(id(list_squares_output[0]),
                            id(list_squares_output[1]))
        self.assertIsNot(s1, list_squares_output[0])
        self.assertIsNot(s2, list_squares_output[1])
        self.assertEqual(s1.id, list_squares_output[0].id)
        self.assertEqual(s1.width, list_squares_output[0].width)
        self.assertEqual(s1.height, list_squares_output[0].height)
        self.assertEqual(s1.x, list_squares_output[0].x)
        self.assertEqual(s1.y, list_squares_output[0].y)
        self.assertEqual(s2.id, list_squares_output[1].id)
        self.assertEqual(s2.width, list_squares_output[1].width)
        self.assertEqual(s2.height, list_squares_output[1].height)
        self.assertEqual(s2.x, list_squares_output[1].x)
        self.assertEqual(s2.y, list_squares_output[1].y)
        Square.save_to_file(None)
        self.assertEqual(Square.load_from_file(), [])
        Square.save_to_file([])
        self.assertEqual(Square.load_from_file(), [])
