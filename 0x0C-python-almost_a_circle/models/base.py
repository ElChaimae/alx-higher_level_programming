#!/usr/bin/python3
"""
Defines a Base Class
"""

import json
import csv


class Base:
    """ This class is the “base” of all other classes in this project """

    __nb_objects = 0

    def __init__(self, id=None):
        """ Class Constructor
        Args:
            id (int): instance identifier
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        It returns the JSON representation of list_dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        It writes the JSON string representation of list_objs to a file
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """
        It returns the list of the JSON string representation json_string
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        It returns an instance with all attributes already set
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    def load_from_file(cls):
        """
        It returns a list of instances
        """
        filename = cls.__name__ + ".json"
        instances = []
        try:
            with open(filename, "r") as file:
                data = file.read()
                if data:
                    json_list = json.loads(data)
                    instances = [cls.create(**item) for item in json_list]
        except FileNotFoundError:
            pass
        return instances
