#!/usr/bin/python3
"""Defines say my name function."""


def say_my_name(first_name, last_name=""):
    """Prints My name is <first name> <last name>

        Args:
            first_name (str): first name to be printed
            last_name (str): last name to be printed

        Raises:
            TypeError: If the first_name or the last_name are not strings

        Returns:
            A Greeting message (My name is <first name> <last name>)
        """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
