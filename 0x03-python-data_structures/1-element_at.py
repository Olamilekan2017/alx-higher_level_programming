#!/usr/bin/python3
def element_at(my_list, idx):
    temp = len(my_list)
    if idx < 0:
        return None
    elif idx >= temp:
        return None
    else:
        return my_list[idx]
