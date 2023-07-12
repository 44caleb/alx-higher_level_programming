#!/usr/bin/python3
"""file i/o function"""


import json


def save_to_json_file(my_obj, filename):
    """
    writes an object to a file using json
    Args:
        my_obj: obj
        filename: file
    """
    with open(filename, "w") as f:
        json.dump(my_obj, f)
