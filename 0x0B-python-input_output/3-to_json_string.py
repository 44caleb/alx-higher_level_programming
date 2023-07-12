#!/usr/bin/python3
"""file i/o function"""


import json


def to_json_string(my_obj):
    """
    returns json form of an object
    Args:
        my_obj: object(string)
    Returns: json
    """
    return json.dumps(my_obj)
