#!/usr/bin/python3
"""Defines a rectangle class."""


from models.base import Base


class Rectangle(Base):
    """Represents a rectangle shape."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialization of the data."""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Set/Get width"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """Set/Get height."""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")

        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """Set/Get x."""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")

        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """Set/Get y."""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")

        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """Returns the area value of the Rectangle instance."""
        return self.__width * self.__height

    def display(self):
        """Prints in stdout the Rectangle instance with the character #"""
        print(self.__y * '\n', end='')
        print(self.__height * (self.__x * ' ' + self.__width * '#' + '\n'),
              end='')

    def __str__(self):
        """String representation of the rectangle."""
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        """Update the data."""
        if args and len(args) > 0:
            try:
                self.id = args[0]
                self.__width = args[1]
                self.__height = args[2]
                self.__x = args[3]
                self.__y = args[4]
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
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y,
        })
