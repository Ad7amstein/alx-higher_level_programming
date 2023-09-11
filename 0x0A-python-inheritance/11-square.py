#!/usr/bin/python3
"""Defines a square class."""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square shape."""

    def __init__(self, size):
        """Initializes the data."""
        self.__size = size

        super().__init__(self.__size, self.__size)

    def area(self):
        """Calculates and return the square area"""
        return (self.__size * self.__size)

    def __str__(self):
        return ("[Square] {}/{}".format(self.__size, self.__size))