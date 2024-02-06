#!/usr/bin/python3
""" A function that returns true or false"""


def is_same_class(obj, a_class):
    """Check if the object is exactly an instance of the specified class """

    if type(obj) == a_class:
        return True
    return False
