#!/usr/bin/python3
"""Defines a base class."""


import json
import csv


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
            json.dump(list_dictionaries, MyFile)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set."""
        from models.rectangle import Rectangle
        from models.square import Square

        if cls.__name__ == 'Rectangle':
            obj = Rectangle(1, 1)
        if cls.__name__ == 'Square':
            obj = Square(1)
        obj.update(**dictionary)
        return obj

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances."""
        filename = cls.__name__ + '.json'
        list_instances = []
        try:
            with open(filename, mode='r', encoding='utf-8') as MyFile:
                objects_dict = cls.from_json_string(MyFile.read())
        except FileNotFoundError:
            return []

        for obj_dict in objects_dict:
            obj = cls.create(**obj_dict)
            list_instances.append(obj)

        return list_instances

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes python objects in csv files."""
        filename = cls.__name__ + '.csv'

        if list_objs is not None or list_objs != []:
            list_dicts = [x.to_dictionary() for x in list_objs]
            header = list_dicts[0].keys()

            with open(filename, 'w', newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=header)
                writer.writeheader()
                writer.writerows(list_dicts)


    @classmethod
    def load_from_file_csv(cls):
        """Deserializes python objects in csv files."""
        filename = cls.__name__ + '.csv'
        list_inctances = []

        try:
            with open(filename, newline='') as csvfile:
                reader = csv.DictReader(csvfile)

                for row in reader:
                    for key in row.keys():
                        row[key] = int(row[key])
                    obj_dict = row.copy()
                    obj = cls.create(**obj_dict)
                    list_inctances.append(obj)

                return list_inctances
        except FileNotFoundError:
            return []


