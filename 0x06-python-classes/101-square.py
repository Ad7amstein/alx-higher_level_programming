#!/usr/bin/python3
"""Defines a class Square."""


class Square:
    """Represents a square, withe a size."""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes the data.

        Args:
            size (int): The size of the new square
            position (tuple): The position of the square
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Get/set the current positino of the square."""
        return self.__position

    @position.setter
    def position(self, position):
        if not isinstance(position, tuple) or len(position) != 2 or \
            not isinstance(position[0], int) or \
            not isinstance(position[1], int) or position[0] < 0 or \
                position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

    def my_print(self):
        """Prints the square"""
        if self.__size == 0:
            print()
        else:
            print(self.__position[1] * '\n', end='')
            print(self.__size * ((self.__position[0] * ' ') +
                                 (self.__size * '#') + '\n'), end='')

    def __str__(self):
        printable_square = self.__position[1] * '\n' + \
            self.__size * ((self.__position[0] * ' ') +
                           (self.__size * '#') + '\n')
        return printable_square
