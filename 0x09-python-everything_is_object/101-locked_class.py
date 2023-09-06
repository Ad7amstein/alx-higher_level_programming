#!/usr/bin/python3
"""Defines a LockedClass."""


class LockedClass:
    """Represents a LockedClass."""

    def __setattr__(self, name, value):
        """Define how setattr should work"""
        if name == "first_name":
            super().__setattr__(name, value)
        else:
            raise AttributeError(
                "'LockedClass' object has no attribute {}".format(name))
