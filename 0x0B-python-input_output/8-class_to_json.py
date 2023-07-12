#!/usr/bin/python3
"""returns dictionary description of an object"""


def class_to_json(obj):
    """
    returns dictionary description
    Args:
        obj: object
    """
    return obj.__dict__
