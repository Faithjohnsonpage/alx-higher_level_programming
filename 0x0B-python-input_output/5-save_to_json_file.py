#!/usr/bin/python3
import json

"""
A module that writes an Object to a text file, using a JSON representation
"""


def save_to_json_file(my_obj, filename):
    """
    Serialize the given object to a JSON-formatted string
    and write it to the specified file.

    Parameters:
    - my_obj: The object to be serialized and saved to the file.
    - filename: The name of the file where the JSON
                representation will be stored.

    Returns: None

    Example:
    >>> data = {'name': 'John', 'age': 30}
    >>> save_to_json_file(data, 'output.json')
    """
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(json.dumps(my_obj))
