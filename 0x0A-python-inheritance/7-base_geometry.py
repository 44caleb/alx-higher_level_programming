#!/usr/bin/python3
"""creates a class"""


class BaseGeometry:
    """creates a geometry class"""

    def area(self):
        """unimplemented area function"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """integer validation
        Args:
            name: name of value
            value: value
        """
        if type(value) != int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
