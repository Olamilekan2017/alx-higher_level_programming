#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list:
        new_list = []
        for num in my_list:
            multiple_of_2 = num % 2 == 0
            new_list.append(multiple_of_2)
        return new_list
