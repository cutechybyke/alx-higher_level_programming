!/usr/bin/python3
""" Here is a Module that contains a function  writes to a text file
"""


def write_file(filename="", text=""):
    """ this is a Function that writes to a text file
    Args:
        filename: filename
        text: text to write
    Raise
        Exception: when the file can be opened
    """

    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
