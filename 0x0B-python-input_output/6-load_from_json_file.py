#!/usr/bin/python3
"""
A module creates an Object from a “JSON file”
"""


import json

def load_from_json_file(filename):
    """
    deserialize the string representation of an object
    """
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            return json.loads(line)
