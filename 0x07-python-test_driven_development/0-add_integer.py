#!/usr/bin/python3
""" This function add two integers """


def add_integer(a, b=98):
    """ Addition function """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    result = a + b
    return result
