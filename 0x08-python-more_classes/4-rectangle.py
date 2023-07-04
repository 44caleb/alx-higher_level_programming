#!/usr/bin/python3
"""initialziation of rectangle"""


class Rectangle:
    """Defines a rectangle"""

    def __init__(self, width=0, height=0):
        """Initializes a rectangle object with a given width and height"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter method to retrieve the width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method to set the width attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter method to retrieve the height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method to set the height attribute"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        return 2 * (self.width + self.height)

    def __str__(self):
        """Returns a string representation of the rectangle"""
        if self.width == 0 or self.height == 0:
            return ""
        rectangle_str = ""
        for _ in range(self.height):
            rectangle_str += "#" * self.width + "\n"
        return rectangle_str.rstrip()

    def __repr__(self):
        """Returns a string representation that can recreate the object"""
        return f"Rectangle({self.width}, {self.height})"
