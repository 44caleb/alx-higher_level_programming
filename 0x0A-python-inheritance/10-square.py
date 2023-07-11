#!/usr/bin/python3
"""creates a rectangle class"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """square class"""

    def __init__(self, size):
        """class initializaatoin
        Args
           size: size of side of square
        """
        super().integer_validator('size', size)
        Rectangle.__init__(self, size, size)
