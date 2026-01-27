#!/usr/bin/python3
def isuppercase(str):
    for c in str:
        if ord(c) in range(97, 123):
           print("{}".format(chr(ord(c) - 32)))
        else:
            print("{}".format(c))
