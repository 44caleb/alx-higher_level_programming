#!/usr/bin/python3
"""file i/o function"""


def append_write(filename="", text=""):
    """
    appends a string at the end of a file
    Args:
        filename: file
        text: string
    """
    with open(filename, mode="a", encoding="UTF8") as f:
        return f.write(text)
