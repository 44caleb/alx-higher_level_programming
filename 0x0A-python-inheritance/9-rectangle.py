#!/usr/bin/python3i
"""creates a class"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """creates a subclass of BaseGeometry"""
    def __init__(self, width, height):
        """
        class instantiation
        Args:
            width: width
            height: height
        """
        if not super().integer_validator('width', width):
            self.__width = width
        if not super().integer_validator('height', height):
            self.__height = height

    def area(self):
        """returns area"""
        return self.__width * self.__height

    def __str__(self):
        """string representation"""
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
