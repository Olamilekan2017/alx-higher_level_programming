#!/usr/bin/python3
""" This function print my name is first name and astname """


def say_my_name(first_name, last_name=""):
    """ Prints first name and last name """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
