#!/usr/bin/python3
""" Defines an object that return a list """
def lookup(obj):
    """ Returns a list containing attributes and methods """

    attributes_method = dir(obj)
    return (attributes_method)
