#!/usr/bin/python3
""" Defines file appending function """


def append_write(filename="", text=""):
    """ Appends a string """

    with open(filename, "a", encoding="utf-8") as a:
        return a.write(text)
