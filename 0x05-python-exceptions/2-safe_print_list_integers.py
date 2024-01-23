#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        if my_list:
            total = 0
            for i in range(x):
                if isinstance(my_list[i], int):
                    print("{:d}".format(my_list[i]), end="")
                    total += 1
            print()
            return total
    except ValueError:
        print()
        return total
