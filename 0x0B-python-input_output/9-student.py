#!/usr/bin/python3
"""creates a class"""


class Student:
    """creates a student class"""
    def __init__(self, first_name, last_name, age):
        """initializes object"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """returns dictonary description of object"""
        return self.__dict__
