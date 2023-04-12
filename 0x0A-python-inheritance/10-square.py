#!/usr/bin/python3
"""
This Contains the class BaseGeometry and subclass Rectangle
"""

Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """this is for the representation of a square"""
    def __init__(self, size):
        """instantiation of the square happens here"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """"here, it returns the area of the square"""
        return self.__size ** 2
