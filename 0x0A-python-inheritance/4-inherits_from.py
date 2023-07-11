#!/usr/bin/python3
"""creates a function"""


def inherits_from(obj, a_class):
    """checks if an object is a subclass
    Args:
        obj: object
        a_class: class
    """
    obj_type = type(obj)
    return obj_type != a_class and issubclass(obj_type, a_class)
