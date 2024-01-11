#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if key in a_dictionary:
        del a_dictionary[key]
        print("Key '{}' deleted successfully.".format(key))
    else:
        print("Key '{}' not found in the dictionary.".format(key))
