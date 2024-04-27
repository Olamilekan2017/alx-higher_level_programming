#!/usr/bin/python3
"""Python script that takes in a URL and an email address"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) > 2:
        encode = [("email", sys.argv[2])]
        ur = requests.post(sys.argv[1], data=encode)
        print(ur.text)
