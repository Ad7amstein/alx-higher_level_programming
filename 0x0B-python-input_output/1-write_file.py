#!/usr/bin/python3
"""Defines a write file function."""


def write_file(filename="", text=""):
    """Writes a string to a text file (UTF8)
        and returns the number of characters written.

    Args:
        filename (txt): The name of the file.
        text (str): text to be written into the file.
    """
    with open(filename, "w", encoding="utf-8") as MyFile:
        return (MyFile.write(text))
