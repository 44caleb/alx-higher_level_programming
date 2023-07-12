#!/usr/bin/python3
"""creates a class"""


class Student:
    """creates a student class"""
    def __init__(self, first_name, last_name, age):
        """initializes object"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """returns dictonary description of object"""
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        "replaces all attributes of object"""
        for key, value in json.items():
            setattr(self, key, value)
