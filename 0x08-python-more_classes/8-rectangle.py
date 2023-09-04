#!/usr/bin/python3
"""Defines a rectangle class."""


class Rectangle:
    """Represents a rectangle shape."""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initializes the rectangle data.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """Set/Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Set/Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the rectangel."""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return (2 * self.__width + 2 * self.__height)

    def __str__(self):
        """Returns a string representation for the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return ''
        printable_string = (
            self.__height *
            (self.__width * str(self.print_symbol) + '\n'))[:-1]
        return printable_string

    def __repr__(self):
        """Returns a string representation of the rectangle
            to be able to recreate a new instance by using eval()
        """
        return 'Rectangle({}, {})'.format(self.__width, self.__height)

    def __del__(self):
        """Prints a small nice message when a ractangle is deleted."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Compares two rectangles and return the bigger
        
        Args:
            rect_1 (Rectangle): First rectangle
            rect_2 (Rectangle): Second rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")

        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
