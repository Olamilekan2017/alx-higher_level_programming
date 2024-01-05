#!/usr/bin/python3
if __name__ == "__main__":
    from hidden_4 import *
    allf = dir()
    for x in range(len(allf)):
        if allf[x][:2] != "__":
            print("{:s}".format(allf[x]))
