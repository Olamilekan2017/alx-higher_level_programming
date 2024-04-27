#!/usr/bin/python3
"""Python script that takes in a URL"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) > 1:
        ur = requests.get(sys.argv[1])
        if "X-Request-Id" in ur.headers:
            print(ur.headers["X-Request-Id"])
