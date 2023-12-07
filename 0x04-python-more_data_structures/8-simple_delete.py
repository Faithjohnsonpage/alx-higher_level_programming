#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    for existing_key in a_dictionary:
        if existing_key == key:
            del existing_key
            break
    return a_dictionary
