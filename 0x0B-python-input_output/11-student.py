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
            d = {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        else:
            d = self.__dict__
        return d

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance."""
        for k, v in json.items():
            setattr(self, k, v)
