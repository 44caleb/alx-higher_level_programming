#!/usr/bin/python3
"""file io functions"""


import json


def load_from_json_file(filename):
    """
    creates an object from JSON file
    Args:
        filename: file
    """
    with open(filename, "r") as f:
        data = json.load(f)
        return data
