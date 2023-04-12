#!/usr/bin/python3
"""
This Contains the inherits_from function
"""

def inherits_from(obj, a_class):
    """This code here returns true  if the obj is a subclass of a_class, otherwise we get a  false"""
    return(issubclass(type(obj), a_class) and type(obj) != a_class)
