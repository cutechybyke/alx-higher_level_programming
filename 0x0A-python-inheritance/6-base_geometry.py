#!/usr/bin/python3
"""
This Contains the class BaseGeometry
"""

class BaseGeometry:
    """Here, we have a class with public attribute area"""
    def area(self):
        """This here raises an exception when it is called"""
        raise Exception("area() is not implemented")
