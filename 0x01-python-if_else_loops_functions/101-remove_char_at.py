#!/usr/bin/python3
def remove_char_at(str, n):
    new_str = ""
    for i, char in enumerate(str):
        if i == n:
            continue
        new_str += char
    return new_str
