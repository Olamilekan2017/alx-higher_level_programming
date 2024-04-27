#!/usr/bin/python3
"""Takes in a URL and an email """
from urllib import request, parse
import sys


if __name__ == "__main__":
    if len(sys.argv) > 2:
        encode = bytes(parse.urlencode([("email", sys.argv[2])]), "utf-8")
        with request.urlopen(sys.argv[1], data=encode) as ur:
            print(ur.read().decode("utf-8"))
