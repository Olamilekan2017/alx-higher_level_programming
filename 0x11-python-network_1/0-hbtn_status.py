#!/usr/bin/python3
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as ur:
        if ur.read():
            urldata = ur.read()
            print("\t- Body response:")
            print("\t\t- type: {}".format(type(urldata)))
            print("\t\t- content: {}".format(urldata))
            print("\t\t- utf8 content: {}".format(urldata.decode('utf-8')))
