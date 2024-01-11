#!/usr/bin/python3
"""
A module that adds all arguments to a Python list
"""


import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


my_list = []

# Load existing data from add_item.json if it exists
try:
    my_list = load_from_json_file("add_item.json")
except FileNotFoundError:
    pass

# Add arguments to the list
my_list.extend(sys.argv[1:])

# Save the updated list to add_item.json
save_to_json_file(my_list, "add_item.json")
