#!/usr/bin/python3
"""Defines an empty class base geometry."""


class BaseGeometry:
    """Represents a Base class Geometry."""

    def area(self):
        """Functino that raises an exception."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates the value.

        Args:
        name (str): name of the variable
        value (int): The integer value

        Raises:
            TypeError: If the value is not integer.
            ValueError: If the value is less than or equal zero.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
