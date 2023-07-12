#!/usr/bin/python3
"""file i/o function"""


def write_file(filename="", text=""):
    """
    write to a text file
    Args:
        filename: file to write to
        text: string to write
    """
    with open(filename, mode="w", encoding="UTF8") as f:
        return f.write(text)
