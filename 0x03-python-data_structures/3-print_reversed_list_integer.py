#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    c = -1
    
    for i in my_list:
        print("{}".format(my_list[c]))
        c = c - 1
