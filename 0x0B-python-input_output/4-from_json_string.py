#!/usr/bin/python3
""" Defines JSON to object """
import json


def from_json_string(my_str):
    """ Return the puthon object rrp of json """

    return json.loads(my_str)
