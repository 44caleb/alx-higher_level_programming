#!/usr/bin/python3
"""Square class definition"""


class Square:
    """Square class definition"""

    def __init__(self, size=0):
        """Initialization of square objects

        Args:
            size (int): square size
        """
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the current square area"""
        return self.__size * self.__size
