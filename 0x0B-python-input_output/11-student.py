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

    def to_json(self, attrs=None):
        my_dict = {}
        if isinstance(attrs, list):
            for attribute in attrs:
                if hasattr(self, attribute):
                    my_dict[attribute] = getattr(self, attribute)
            return my_dict
        return self.__dict__

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance
        with values from a JSON dictionary.

        Args:
            json(dict): A dictionary representing the
            new values for the attributes.
        """
        if isinstance(json, dict):
            for key, value in json.items():
                setattr(self, key, value)
