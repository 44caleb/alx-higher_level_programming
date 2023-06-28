#!/usr/bin/python3
"""Square class definition"""


class Square:
    """Square class definition"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialization of square objects

        Args:
            size (int): square size
            position (tuple): position of the square
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2 or \
           not all(isinstance(num, int) for num in value):
            raise TypeError("position must be a tuple of two integers")
        if any(num < 0 for num in value):
            raise ValueError("position values must be >= 0")
        self.__position = value

    def area(self):
        """Returns the current square area"""
        return self.__size * self.__size

    def my_print(self):
        """Prints a square based on the size and position attributes"""
        if self.__size == 0:
            print("")
            return

        for _ in range(self.__position[1]):
            print("")
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
