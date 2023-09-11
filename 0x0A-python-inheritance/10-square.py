#!/usr/bin/python3
"""Defines a square class."""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square shape."""

    def __init__(self, size):
        """Initializes the data."""
        super().__init__(size, size)

        self.__size = size

