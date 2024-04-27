#!/usr/bin/python3
"""Takes in a URL, sends a request to the URL"""
from urllib import request, error
import sys


if __name__ == "__main__":
    if len(sys.argv) > 1:
        try:
            with request.urlopen(sys.argv[1]) as ur:
                print(ur.read().decode("utf-8"))
        except error.HTTPError as httperror:
            print("Error code: {}".format(httperror.code))
