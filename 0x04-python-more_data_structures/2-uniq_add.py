#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    seen = []
    for i in my_list:
        if i in seen:
            sum = sum + 0
        else:
            sum = sum + i
            seen.append(i)
    return sum
