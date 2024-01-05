#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    sumint = 0
    x = len(argv) - 1
    if x < 1:
        print("{}".format(x))
    else:
        for i in range(x):
            sumint += int(argv[i + 1])
        print("{:d}".format(sumint))
