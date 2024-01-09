#!/usr/bin/python3
"""
A module that appends a string at the end of a text file (UTF8)
"""


def append_write(filename="", text=""):
    """
    Function returns the number of characters added
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
