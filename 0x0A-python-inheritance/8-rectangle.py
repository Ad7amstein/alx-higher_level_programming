#!/usr/bin/python3
"""Defines a rectangle calss."""


class Rectangle(__import__('7-base_geometry').BaseGeometry):
    """Represents a rectangle class."""

    def __init__(self, width, height):
        """Initialization of the data"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
