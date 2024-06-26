#!/usr/bin/python3
"""Python script that takes in a URL"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) > 1:
        ur = requests.get(sys.argv[1])
        urlstatus = ur.status_code
        if urlstatus > 399:
            print("Error code: {}".format(urlstatus))
        else:
            print(ur.text)
