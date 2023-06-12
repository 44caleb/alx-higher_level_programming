#!/usr/bin/python3
def no_c(my_string):
    w_list = [x for x in my_string if x not in "cC"]
    new_string = "".join(w_list)
    return new_string
