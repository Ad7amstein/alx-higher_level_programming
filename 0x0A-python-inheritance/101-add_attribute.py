#!/usr/bin/python3
"""Defines add attribute function."""


def add_attribute(obj, name, value):
    """Add a new attribute to obj if it possible.

    Args:
        name (str): The name of the attribute.
        value (any): The value of the attribute.

    Raises:
        TypeError: If the object can't have an attribute.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
