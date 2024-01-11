#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    a_dictionary = {key: v for key, v in a_dictionary.items() if v != value}
    return a_dictionary
