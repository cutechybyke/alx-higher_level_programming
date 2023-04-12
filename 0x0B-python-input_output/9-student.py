#!/usr/bin/python3
""" this is a module that defines the class Student
"""


class Student:
    """ This is a class to create student instances """

    def __init__(self, first_name, last_name, age):
        """ this is a special method to initialize """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Here, we have a method that returns directory description """
        return self.__dict__.copy()
