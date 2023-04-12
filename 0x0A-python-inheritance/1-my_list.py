#!/usr/bin/python3
"""
This here, contains the MyList class
"""


class MyList(list):
    """this is  a subclass of list"""
    def __init__(self):
        """for initializing the object"""
        super().__init__()

    def print_sorted(self):
        """here, this prints the sorted list we want"""
        print(sorted(self))
