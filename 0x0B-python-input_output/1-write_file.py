#!/usr/bin/python3
""" This is a module that contains a function that writes to a text file
"""


def write_file(filename="", text=""):
    """ this is a function that writes to a text file
    Args:
        filename: filename
        text: text to write
    Raise
        Exception: when the file can be opened
    """

    with open(filename, 'w', encoding="utf-8") as f:
