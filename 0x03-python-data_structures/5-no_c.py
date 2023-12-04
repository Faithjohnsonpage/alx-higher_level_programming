#!/usr/bin/python3
def no_c(my_string):
    new_string = ''
    for char in my_string:
        if char == chr(99) or char == chr(67):
            continue
        new_string += char
    return new_string
