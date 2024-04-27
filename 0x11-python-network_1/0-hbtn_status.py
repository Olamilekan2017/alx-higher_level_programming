#!/usr/bin/python3
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as ur:
        if ur.read():
            urldata = ur.read()
            print("Body response:")
            print("\t- type: {}".format(type(urldata)))
            print("\t- content: {}".format(urldata))
            print("\t- utf8 content: {}".format(urldata.decode('utf-8')))
