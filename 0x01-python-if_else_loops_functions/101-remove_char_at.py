#!/usr/bin/python3
def remove_char_at(str, n):
    new_str = ""
    for i in str:
        if i == n:
            continue
        new_str += i
    return new_str
