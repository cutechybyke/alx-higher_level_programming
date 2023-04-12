#!/usr/bin/python3
"""
This Contains the class MyInt
"""

class MyInt(int):
    """This is a rebel version of an integer,which is  perfect for opposite day!"""
    def __new__(cls, *args, **kwargs):
        """This creates a new instance of the class"""
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __eq__(self, other):
        """here, we make what was != is now =="""
        return int(self) != other

    def __ne__(self, other):
        """here, what was == is now !="""
        return int(self) == other
