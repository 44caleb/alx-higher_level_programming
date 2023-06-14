#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    key = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    total = 0
    for i in range(0, len(roman_string)):
        if i < (len(roman_string) - 1):
            if key[roman_string[i]] < key[roman_string[i + 1]]:
                num = -(key[roman_string[i]])
            else:
                num = key[roman_string[i]]
            total += num
        else:
            num = key[roman_string[i]]
            total += num
    return total
