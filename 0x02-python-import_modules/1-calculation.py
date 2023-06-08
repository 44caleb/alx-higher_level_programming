#!/usr/bin/python3 
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div

    a = 10
    b = 5
    plus = add(a, b)
    minus = sub(a, b)
    prod = mul(a, b)
    divide = div(a, b)

    print("{} + {} = {}".format(a, b, plus))
    print("{} - {} = {}".format(a, b, minus))
    print("{} * {} = {}".format(a, b, prod))
    print("{} / {} = {}".format(a, b, divide))
