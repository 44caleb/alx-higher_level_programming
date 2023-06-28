#!/usr/bin/python3
"""Square class definition"""


class Square:
    """square class definition"""
    def __init__(self, size=0):
        """initialization of square objects

        Args:
            size (int): square size
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """returns the current square area"""
        return self.__size * self.__size
