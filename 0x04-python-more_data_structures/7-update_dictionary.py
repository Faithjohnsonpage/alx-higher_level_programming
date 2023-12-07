#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    for existing_key in a_dictionary:
        if existing_key == key:
            a_dictionary[existing_key] = value
            break  # Break out of the loop once the key is found
    else:
        # If the loop completes without breaking, the key was not found
        a_dictionary[key] = value

    return a_dictionary
