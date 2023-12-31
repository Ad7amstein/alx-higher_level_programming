#!/usr/bin/python3
"""Defines a MagicClass"""

import math


class MagicClass:
    """Represents a MagicClass"""

    def __init__(self, radius=0):
        """Initializing a MagicClass

        Args:
            radius (float or int): The radius of the new MagicClass object"""
        self.__radius = 0

        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")

        self.__radius = radius

    def area(self):
        """Calculates the area

        Returns:
            float: The area
        """
        return ((self.__radius ** 2) * math.pi)

    def circumference(self):
        """Calculates the circumference

        Returns:
            float: The circumference
        """
        return (2 * math.pi * self.__radius)
