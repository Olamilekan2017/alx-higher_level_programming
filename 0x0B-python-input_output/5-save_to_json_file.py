#!/usr/bin/python3
""" Defines a Json file-writting """
import json


def save_to_json_file(my_obj, filename):
    """ write an object to json text file """

    with open(filename, "w") as i:
        json.dump(my_obj, i)
