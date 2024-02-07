#!/usr/bin/python3
""" Defines JSON file-reading """
import json


def load_from_json_file(filename):
    """ Return the puthon o@bject rrp of json """

    with open(filename) as i:
        return json.loads(i)
