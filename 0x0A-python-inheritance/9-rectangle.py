#!/usr/bin/python3
"""
This Contains the class BaseGeometry and subclass Rectangle
"""

class BaseGeometry:
    """this is a class with public instance methods area and integer_validator"""
    def area(self):
        """this here raises an exception when called"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """this here validates that value is an integer greater than 0"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """this is a representation of a rectangle"""
    def __init__(self, width, height):
        """here is for the instantiation of the rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """this returns the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """this is an informal string representation of the rectangle"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
