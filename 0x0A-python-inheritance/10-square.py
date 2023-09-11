#!/usr/bin/python3
"""Defines a square class."""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square shape."""

    def __init__(self, size):
        """Initializes the data."""
        super().integer_validator("size", size)
        self.__size = size

        super().__init__(self.__size, self.__size)

