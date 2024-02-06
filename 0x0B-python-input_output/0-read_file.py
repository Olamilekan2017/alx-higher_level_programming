#!/usr/bin/python3
""" Defines a function text file-reading """


def read_file(filename=""):
    with open(filename, encoding="utf-8") as i:
        print(i.read(), end="")
