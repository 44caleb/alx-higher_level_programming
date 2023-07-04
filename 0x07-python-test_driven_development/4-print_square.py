#!/usr/bin/python3
"""functoin that prints a square character"""


def print_square(size):
    """
    prints a square character
    Args:
        size (int): length of square
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise TypeError("size must be an integer")
    for row in range(0, size):
        print("#" * size)
