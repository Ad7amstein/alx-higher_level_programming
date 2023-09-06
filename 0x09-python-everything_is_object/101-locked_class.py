#!/usr/bin/python3
"""Defines a LockedClass."""


class LockedClass:
    """Represents a LockedClass.
    Prevents a user from making new attributes that his name is not
    `first_name`"""

    def __setattr__(self, name, value):
        """Define how setattr should work."""
        if name == 'first_name':
            self.__dict__[name] = value
        else:
            raise AttributeError(
                "'LockedClass' object has no attribute '{}'".format(name))
