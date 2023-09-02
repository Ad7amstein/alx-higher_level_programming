#!/usr/bin/python
"""Defines a print square function."""


def print_square(size):
    """Prints a square with the character #.

    Args:
        size (int): Size length of the square.

    Raises:
        TypeError: If the size is not integer
        TypeError: If the size is not integer and less than 0
        ValueError: If the size is less than 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if size == 0:
        print()
    else:
        print(size * (size * '#' + '\n'), end='')
