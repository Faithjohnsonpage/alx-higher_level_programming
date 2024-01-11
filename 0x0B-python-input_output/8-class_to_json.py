#!/usr/bin/python3
"""
A module that converts an object into JSON-like dictionary
"""


def class_to_json(obj):
    """
    Returns a JSON-like dictionary
    """
    return obj.__dict__
