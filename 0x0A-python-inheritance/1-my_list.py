#!/usr/bin/python3
""" Defines a function with the class MyList """


class MyList(list):
    """ MyList that inherits from list """

    def print_sorted(self):
        """ Print a list in sorting ascending order """
        print(sorted(self))
