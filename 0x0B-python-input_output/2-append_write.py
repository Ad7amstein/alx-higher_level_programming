#!/usr/bin/python3
"""Defines an append write function."""


def append_write(filename="", text=""):
    """Appends a string at the end of a text file (UTF8)
        and returns the number of characters added

    Args:
        filename (txt): The name of the file.
        text (str): text to be written into the file.
    """
    with open(filename, "a", encoding="utf-8") as MyFile:
        return (MyFile.write(text))
