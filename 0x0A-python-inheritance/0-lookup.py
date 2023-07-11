#!/usr/bin/python3
""" creates a function that returns attributes """


def lookup(obj):
    """
    checks the attributes of an object
    Args:
        obj: object of any class
    Returns:
        list of attributes and methods
    """
    return dir(obj)
