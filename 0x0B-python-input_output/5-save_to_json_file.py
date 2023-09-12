#!/usr/bin/python3
"""Defines a save_to_json_file function."""


import json


def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file,
        using a JSON representation

    Args:
        my_obj (any): Object to be written
        filename (str): File to write in.
    """
    with open(filename, "w", encoding="utf-8") as MyFile:
        json.dump(my_obj, MyFile)
