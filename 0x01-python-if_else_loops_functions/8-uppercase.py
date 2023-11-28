#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if ord(c) in range(97, 123):
            char = ch(ord(c)-32)
        else:
            char = c
            print("{}".format(char), end='')
            print("{}".format(''))

