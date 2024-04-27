#!/usr/bin/python3
""" Python script that fetches https://alx-intranet.hbtn.io/status """
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as ur:
        if ur.read():
            urldata = ur.read()
            print("Body response:")
            print(f"\t- type: {type(urldata)}")
            print(f"\t- content: {urldata}")
            print(f"\t- utf8 content: {urldata.decode('utf-8')}")
