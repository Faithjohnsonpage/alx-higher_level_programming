#!/usr/bin/python3

def uniq_add(my_list=[]):
    sum = 0
    unique_set = set(my_list)
    for i in unique_set:
        sum += i
    return sum
