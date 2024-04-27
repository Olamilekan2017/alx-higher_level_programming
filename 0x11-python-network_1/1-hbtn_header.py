#!/usr/bin/python3
"""Takes in a URL, sends a request to URL and displays value X-Request-Id"""
import urllib.request
import sys


if __name__ == "__main__":
    if len(sys.argv) > 1:
        with urllib.request.urlopen(sys.argv[1]) as ur:
            print(ur.headers["X-Request-Id"])
