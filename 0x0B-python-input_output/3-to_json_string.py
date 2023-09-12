#!/usr/bin/python3
"""Defines a to json string function."""


import json


def to_json_string(my_obj):
    """Returns the JSON representation of an object (string).

    Args:
        my_obj (any): Object to return it's Json.
    """
    return (json.dumps(my_obj))
