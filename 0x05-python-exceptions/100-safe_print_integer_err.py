#!/usr/bin/python3
from sys import stderr


def safe_print_integer_err(value):
    try:
        # Attempt to print the value as an integer
        print("{:d}".format(value))
    except (ValueError, TypeError) as e:
        # Handle the exception if the value is not an integer
        print("Exception: {}".format(e), file=stderr)
        return False
    else:
        return True
