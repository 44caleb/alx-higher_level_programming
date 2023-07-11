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
        if super().integer_validator('width', width):
            self.__width = width
        if super().integer_validator('height', height):
            self.__height = height
