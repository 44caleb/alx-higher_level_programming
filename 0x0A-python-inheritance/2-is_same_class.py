#!/usr/bin/python3
"""contains function to check class instance"""


def is_same_class(obj, a_class):
    """
    check if an object belongs to a class
    Args:
        obj: object of any class
        a_class: class to check for
    Returns:
        True if object belongs to class
        False otherwise
    """
    return (type(obj) is a_class)
