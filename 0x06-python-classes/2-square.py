#!/usr/bin/python3
""" defines a square class """


class Square:
    """Square class definition """
    def __init__(self, size=0):
        """initializes square objects
        Args:
            size (int): square size
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
