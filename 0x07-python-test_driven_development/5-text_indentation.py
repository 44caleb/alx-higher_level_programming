#!/usr/bin/python3
"""function that prints a text with new lines"""


def text_indentation(text):
    """
    prints text with newline after certain characters
    Arg:
        text(str): text to print
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    i = 0
    while i < len(text):
        if text[i] in [".", "?", ":"]:
            print(text[i], end="")
            print()
            print()
            i += 2
        else:
            print(text[i], end="")
            i += 1
