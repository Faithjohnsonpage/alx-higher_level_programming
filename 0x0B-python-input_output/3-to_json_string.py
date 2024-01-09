#!/usr/bin/python3
"""
A module returns the JSON representation of an object (string)
"""

import json


def to_json_string(my_obj):
    """
    Returns the string representation
    """
    return json.dumps(my_obj)
