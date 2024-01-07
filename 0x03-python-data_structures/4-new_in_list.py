#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    modified_list = my_list[:]
    temp = len(my_list)
    if idx < 0:
        return modified_list
    if idx >= temp:
        return modified_list
    else:
        modified_list[idx] = element
        return modified_list
