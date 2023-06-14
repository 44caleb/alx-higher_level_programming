#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = a_dictionary.copy()
    for i in new_dict:
        value = new_dict[i] * 2
        new_dict[i] = value
    return new_dict
