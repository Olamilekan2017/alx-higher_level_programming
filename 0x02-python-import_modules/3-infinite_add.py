#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    sumint = 0
    x = len(argv) - 1
    for i in range(x):
        sumint += int(argv[i + 1])
    print("{:d}".format(sumint))
