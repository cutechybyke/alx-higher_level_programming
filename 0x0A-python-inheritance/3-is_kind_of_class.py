#!/usr/bin/python3
"""
This Contains the is_kind_of_class function
"""

def is_kind_of_class(obj, a_class):
    """here, we get a True if obj is an instance or inherited from a_class, else we get a  False"""
    return (isinstance(obj, a_class))
