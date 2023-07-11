#!/usr/bin/python3
""" creates a new class """


class MyList(list):
    """creates a subclass of list class"""

    def print_sorted(self):
        """
        prints a sorted list
        """
        print(sorted(self))
