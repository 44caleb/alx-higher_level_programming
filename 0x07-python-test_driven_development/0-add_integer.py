#!/usr/bin/python3
"""function that adds 2 integers"""


def add_integer(a, b=98):
    """
    adds two integers and returns the sum
    Args:
        a (int): first parameter
        b (int): second parameter
    Returns:
        int: the sum of and b
    Raises:
        TypeError: if a is not specified or the arguments are not numbers
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
