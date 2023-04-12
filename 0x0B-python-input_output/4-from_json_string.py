#!/usr/bin/python3
""" This is a module that contains a function that returns an object by
a JSON representation
"""
import json


def from_json_string(my_str):
    """ this is a function that returns an object by a JSON representation
    Args:
        my_str: JSON representation
    Raises:
        Exception: this is when the string can't be decoded
    """
    return json.loads(my_str)
