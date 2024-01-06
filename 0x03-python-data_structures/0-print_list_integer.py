#!/usr/bin/python3
def print_list_integer(my_list=[]):
    temp = len(my_list)
    for i in range(temp):
        print("{:d}".format(my_list[i]))
