#!/usr/bin/python3
""" This function writes an empty list """


class BaseGeometry:
    """ Represent the class basegeometry """

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
