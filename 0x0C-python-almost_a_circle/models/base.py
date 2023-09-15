#!/usr/bin/python3
"""Defines a base class."""


import json


class Base:
    """Represents a base class."""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialization of the data."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries."""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file."""
        filename = cls.__name__ + ".json"
        list_dictionaries = []

        if list_objs is not None or list_objs != []:
            for obj in list_objs:
                obj = obj.to_dictionary()
                list_dictionaries.append(obj)

        with open(filename, mode="w", encoding="utf-8") as MyFile:
            json.dump(cls.to_json_string(list_dictionaries), MyFile)
