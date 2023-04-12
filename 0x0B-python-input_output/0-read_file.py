#!/usr/bin/python3
""" Here is a module that contains a function that reads from a file """


def read_file(filename=""):
    """ this is a function that reads from a file
    Args:
        filename: filename
    Raises
        Exception: this occurs when the file can be opened
    """

    with open(filename, 'r', encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end='')
