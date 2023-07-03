#!/usr/bin/python3
"""creates a rectangle class"""


class Rectangle:
    """creates rectangle class"""

    def __init__(self, width=0, height=0):
        """initializes rectangle objects"""
        self.__width = width
        self.__height = height

    def area(self):
        """returns the rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """returns the rectangle area"""
        return (2 * (self.__width + self.__height))

    @property
    def width(self):
        """
        Getter method which retrieves the width attribute

        Returns:
        int: width of the rectangle
        """
        return self.__width

    @property
    def height(self):
        """Getter method which retrieves the height attribute"""
        return self.__height

    @width.setter
    def width(self, value):
        """Setter method to set width attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Setter method to set height attribute"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
