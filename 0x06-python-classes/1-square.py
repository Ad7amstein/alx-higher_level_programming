#!/usr/bin/python3
"""Defines a class Square."""


class Square:
    """Represents a square, withe a size."""

    def __init__(self, size):
        """Initializes the data.

        Args:
            size (int): The size of the new square.
        """
        self.__size = size
