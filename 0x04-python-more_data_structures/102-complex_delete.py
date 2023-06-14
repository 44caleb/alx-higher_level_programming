#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    new_dict = a_dictionary.copy()
    for i in new_dict:
        if new_dict[i] == value:
            del a_dictionary[i]
    return a_dictionary
