#!/usr/bin/python3
"""file i/o function"""


def read_file(filename=""):
    """
    reads a file and prints content
    Args:
        filename: file
    """
    with open(filename, mode="r", encoding="UTF8") as f:
        content = f.read()
        print(content)
