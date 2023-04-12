#!/usr/bin/python3
""" This is a module that contains a function that returns the JSON
representation of an object
"""
import json


def to_json_string(my_obj):
    """ Here is a Function that returns the JSON representation of an object
    Args:
        my_obj: object
    Raise:
        Exception: when the object can't be encoded
    """
    return json.dumps(my_obj)
