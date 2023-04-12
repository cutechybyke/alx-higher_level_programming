#!/usr/bin/python3
""" this is a module that writes an Object to a text file using
a JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """ this is for a function that writes an object to a text file
    by a JSON representation
    Args:
        my_obj: object
        filename: textfile name
    Raise:
        Exception: This is when the object can't be encoded
    """
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
