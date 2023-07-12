#!/usr/bin/python3
"""file i/o functions"""


import json


def from_json_string(my_str):
    """
    returns python object from JSON
    Args:
        my_str: JSON string
    """
    return json.loads(my_str)
