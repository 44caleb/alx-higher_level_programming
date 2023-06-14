#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    _all = set_1.union(set_2)
    new_set = []
    for i in _all:
        if i not in set_1 or i not in set_2:
            new_set.append(i)
    return set(new_set)
