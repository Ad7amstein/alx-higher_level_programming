#!/usr/bin/python3
"""Defines a class square."""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a square shape."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialization of the data."""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """String representation of the square"""
        return ("[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width))

    @property
    def size(self):
        """Set/Get size."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the data."""
        if args and len(args) > 0:
            try:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            except IndexError:
                pass
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    self.__setattr__(key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle."""
        return ({
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y,
        })
