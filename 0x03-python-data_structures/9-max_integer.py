#!/usr/bin/python3

def max_integer(my_list=[]):
    if my_list:
        max_value = my_list[0]

        for value in my_list[1:]:
            if value > max_value:
                max_value = value
        return max_value
    else:
        return None
