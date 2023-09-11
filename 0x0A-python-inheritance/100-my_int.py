#!/usr/bin/python3
"""Defines my int class."""


class MyInt(int):
    """Represents my int class inherits int."""

    def __eq__(self, value):
        """Overrides == operator."""
        return (self.real != value)

    def __ne__(self, value):
        """Overrides != operator."""
        return (self.real == value)
