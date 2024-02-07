#!/usr/bin/python3
""" Defijes a class student """


class Student:
    """ Representbthe student """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, att=None):
        if (type(att) == list and all(type(ele) == str for ele in att)):
            return {i: getattr(self, i) for i in att if hasattr(self, i)}
        return self.__dict__

    def reload_from_json(self, json):
        for i, j in json.items():
            setattr(self, i, j)
