#!/usr/bin/python3
"""
A module that  that defines a student
"""


class Student:
    """A class"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attr=None):
        my_dict = {}
        if isinstance(attr, list):
            for attribute in attr:
                if hasattr(self, attribute):
                    my_dict[attribute] = getattr(self, attribute)
            return my_dict
        return self.__dict__
