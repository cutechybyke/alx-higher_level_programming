!/usr/bin/python3
""" This is a module that returns the dictionary description with a simple
data structure for a JSON serialization of an object
"""


def class_to_json(obj):
    """ Here, we have a function that retuns the dictionary description of an obj """

    res = {}
    if hasattr(obj, "__dict__"):
        res = obj.__dict__.copy()
    return 
