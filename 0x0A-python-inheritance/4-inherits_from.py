#!/usr/bin/python3
""" Write a function that returns true or false """


def inherits_from(obj, a_class):
    """ Check if the object is an instance """

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
