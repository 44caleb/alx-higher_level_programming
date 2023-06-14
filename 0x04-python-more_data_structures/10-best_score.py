#!/usr/bin/python3
def best_score(a_dictionary):
    best = 0
    if not a_dictionary:
        return None
    for i in a_dictionary:
        if not a_dictionary[i]:
            return None
        if a_dictionary[i] > best:
            best = a_dictionary[i]
            person = i
    return person
