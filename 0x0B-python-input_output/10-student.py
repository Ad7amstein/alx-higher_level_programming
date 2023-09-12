#!/usr/bin/python3
"""Defines a student class."""


class Student:
    """Represents a student."""

    def __init__(self, first_name, last_name, age):
        """Initialization of the data."""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance."""
        d = dict()
        if (type(attrs) is list
            and all(type(x) is str for x in attrs)):
            for x in attrs:
                if hasattr(self, x):
                    d[x] = self.__dict__[x]
        else:
            d = self.__dict__
        return d
