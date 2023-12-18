#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    printed_elements = 0
    try:
        for index, value in enumerate(my_list):
            if x > index:
                print("{}".format(value), end="")
                printed_elements += 1
        print()
    except IndexError:
        pass
    return printed_elements
