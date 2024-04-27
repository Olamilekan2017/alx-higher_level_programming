#!/usr/bin/python3
"""Python script that takes your GitHub credentials (username and password"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) > 2:
        urdt = "https://api.github.com/user"
        api_headers = {
                "Accept": "application/vnd.github.v3+json",
                "Username": sys.argv[1],
                "Authorization": "token {}".format(sys.argv[2])
                }
        ur = requests.get(urdt, headers=api_headers)
        urlstatus = ur.status_code
        if urlstatus == 200:
            github_user = ur.json()
            if github_user["login"] == username:
                print(github_user["id"])
            else:
                print("None")
        else:
            print("None")
