#!/usr/bin/python3
import sys

# Check if there are any arguments
if len(sys.argv) == 1:
    print("0 arguments.")
else:
    # Print the number of arguments
    if len(sys.argv) == 2:
        print("{:d} argument:".format(len(sys.argv) -1))
    else:
        print("{:d} arguments:".format(len(sys.argv) - 1))

    # Print each argument
    for index, argument in enumerate(sys.argv[1:], start=1):
        print("{:d}: {:s}".format(index, argument))
