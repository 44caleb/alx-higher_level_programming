#!/usr/bin/python3
def common_elements(set_1, set_2):
    unique = []
    _all = set_1.union(set_2)
    for i in _all:
        if i in set_1 and i in set_2:
            unique.append(i)
    return set(unique)
