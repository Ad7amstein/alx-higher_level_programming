#!/usr/bin/python3
"""Defines a read file function."""


def read_file(filename=""):
    """Reads a text file (UTF8) and prints it to stdout."""
    with open(filename, "r", encoding="utf-8") as MyFile:
        print(MyFile.read(), end="")
