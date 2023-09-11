#!/usr/bin/python3
"""Defines my list class"""


class MyList(list):
    """Class my list that inherits from list."""

    def print_sorted(self):
        """Prints the list in sorted order (ascending sort)."""
        print(sorted(self))
