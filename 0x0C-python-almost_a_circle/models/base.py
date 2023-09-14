#!/usr/bin/python3
"""Defines a base class."""


class Base:
    """Represents a base class."""
    __nb_objects = 0
    def __init__(self, id=None):
        """Initialization of the data."""
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects
