#!/usr/bin/python3
"""creates a function"""


def is_kind_of_class(obj, a_class):
    """
    checks if object is an instance of class
    Args:
        obj: object
        a_class: class
    Returns:
        True or false
    """
    return isinstance(obj, a_class)
