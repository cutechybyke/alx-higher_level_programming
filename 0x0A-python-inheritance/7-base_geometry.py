#!/usr/bin/python3
"""
This here Contains the class BaseGeometry
"""

class BaseGeometry:
    """Here, we have a class with public instance methods area and integer_validator"""
    def area(self):
        """This raises an exception when called"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """This here, validates that value is an integerthat is greater than 0"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
