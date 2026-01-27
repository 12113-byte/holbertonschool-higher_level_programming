#!/usr/bin/python3
def isuppercase(str):
    result = ""
    for c in str:
        if ord(c) in range(97, 123):
            result += chr(ord(c) - 32)
        else:
            result += c
    print(result)
