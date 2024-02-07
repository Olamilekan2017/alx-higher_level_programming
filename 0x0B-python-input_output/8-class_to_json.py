#!/usr/bin/python3
""" Defines a python class to json """


def class_to_json(obj):
    """ Return dict representation """

    return obj.__dict__
