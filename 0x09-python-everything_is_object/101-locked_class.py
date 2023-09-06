#!/usr/bin/python3
"""Defines a LockedClass."""


class LockedClass:
    """Represents a LockedClass.
    Prevents a user from making new attributes that his name is not
    `first_name`"""

    __slots__ = ['first_name']
