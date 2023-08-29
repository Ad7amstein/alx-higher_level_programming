#!/usr/bin/python3
"""Defines a class Square."""


class Square:
    """Represents a square, withe a size."""

    def __init__(self, size=0):
        """Initializes the data.

        Args:
            size (int): The size of the new square
        """
        self.size = size

    def area(self):
        """Calculates and returns the square area"""
        return self.__size * self.__size

    @property
    def size(self):
        """Get/set the current size of the square."""
        return self.__size

    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def __lt__(self, other):
        """Check if the current object's size
        is less than the size of another object.

        Args:
            other: Another object to compare the size against.

        Returns:
            bool: True if the current object's size
            is less than the size of the other object,
                  False otherwise.
        """
        return self.__size < other.size

    def __le__(self, other):
        """Check if the current object's size
        is less than or equal the size of another object.

        Args:
            other: Another object to compare the size against.

        Returns:
            bool: True if the current object's size
            is less than or equal the size of the other object,
                  False otherwise.
        """
        return self.__size <= other.size

    def __eq__(self, other):
        """Check if the current object's size
        is equal to the size of another object.

        Args:
            other: Another object to compare the size against.

        Returns:
            bool: True if the current object's size
            is equal to the size of the other object,
                  False otherwise.
        """
        return self.__size == other.size

    def __ne__(self, other):
        """Check if the current object's size
        is not equal to the size of another object.

        Args:
            other: Another object to compare the size against.

        Returns:
            bool: True if the current object's size
            is not equal to the size of the other object,
                  False otherwise.
        """
        return self.__size != other.size

    def __gt__(self, other):
        """Check if the current object's size
        is greater than the size of another object.

        Args:
            other: Another object to compare the size against.

        Returns:
            bool: True if the current object's size
            is greater than the size of the other object,
                  False otherwise.
        """
        return self.__size > other.size

    def __ge__(self, other):
        """Check if the current object's size
        is greater than or equal the size of another object.

        Args:
            other: Another object to compare the size against.

        Returns:
            bool: True if the current object's size
            is greater than or equal the size of the other object,
                  False otherwise.
        """
        return self.__size >= other.size
