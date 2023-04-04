#!/usr/bin/python3
# 101-locked_class.py

class LockedClass:
    """
    this is to Prevent the user from instantiating new LockedClass(es) attributes
    for anything.
    """

    __slots__ = ["first_name"]
