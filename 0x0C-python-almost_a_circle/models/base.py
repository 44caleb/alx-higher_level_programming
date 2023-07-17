#!/usr/bin/python3
"""creates a base class"""


import json


class Base:
    """creates a base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """base class constructor"""
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns json string of dictionaries"""
        if not list_dictionaries:
            return('[]')
        else:
            return(json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """writes json representation to a file"""
        filename = "{}.json".format(cls.__name__)
        data = []
        if list_obj is None:
            json_data = to_json_string(data)
        else:
            for i in list_objs:
                data.append(i.to_dictionary())
            json_data = to_json_string(data)
        with open(filename, "w") as f:
            f.write(json_data)

    @staticmethod
    def from_json_string(json_string):
        """returns python object from json string"""
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with set attributes"""
        instance = cls(4, 4, 4, 4)
        instance.update(**dictionary)
        return instance
