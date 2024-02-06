#!/usr/bin/python3
""" Defines the function of a file-writting """


def write_file(filename="", text=""):
    """ write a string to the the file """

    with open(filenane, "w", encoding="utf-8") as f:
        return f.write(text)
