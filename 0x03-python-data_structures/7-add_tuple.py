#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    tuple_c = ()

    tuple_a = tuple_a + (0, 0)
    tuple_b = tuple_b + (0, 0)

    # If tuples have more than two elements, consider extra elements
    tuple_a = tuple_a[:2]
    tuple_b = tuple_b[:2]

    for a, b in zip(tuple_a, tuple_b):
        tuple_c += (a + b,)

    return tuple_c
