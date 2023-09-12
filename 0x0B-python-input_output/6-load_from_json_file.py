#!/usr/bin/python3
"""Defines a load_from_json_file"""


import json


def load_from_json_file(filename):
    """Creates an Object from a JSON file.

    Args:
        filename (str): JSON file.
    """
    with open(filename, "r", encoding="utf-8") as MyFile:
        return (json.load(MyFile))
