#!/usr/bin/python3
"""Defines a class Square."""


class Square:
    """Represents a square, withe a size."""

    def __init__(self, size=0):
        """Initializes the data.

        Args:
            size (int): The size of the new square
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Calculates and returns the square area"""
        return self.__size * self.__size
