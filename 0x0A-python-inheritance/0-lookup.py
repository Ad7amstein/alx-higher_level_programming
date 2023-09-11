#!/usr/bin/python3
"""Defines a lookup function."""


def lookup(obj):
    """Returns the list of available attributes and methods of an object

        Args:
            obj (object): The object to return the list to it
    """
    return (dir(obj))
