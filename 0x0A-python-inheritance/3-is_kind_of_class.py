#!/usr/bin/python3
""" Write a function that returns true or false """


def is_kind_of_class(obj, a_class):
    """ Check if the object is an instance """

    if isinstance(obj, a_class):
        return True
    return False
