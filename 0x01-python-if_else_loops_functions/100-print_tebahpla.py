#!/usr/bin/python3
for char in range(ord('z'), ord('a') - 1, -2):
    print("{}{}".format(chr(char), chr(char - 33)), end='')
