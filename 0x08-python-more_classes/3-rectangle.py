#!/usr/bin/python3
"""Defines a rectangle class."""


class Rectangle:
    """Represents a rectangle shape."""

    def __init__(self, width=0, height=0):
        """Initializes the rectangle data.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.width = width
        self.height = height

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
        printable_string = (self.__height * (self.__width * '#' + '\n'))[:-1]
        return printable_string
