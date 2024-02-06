#!/usr/bin/python3
""" Defines a function text file-reading """


def read_file(filename=""):
    """ Prints the details of UTF8 text file """

    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
