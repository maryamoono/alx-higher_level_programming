#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        ule1 = (len(sentence), None)
    else:
        ule1 = (len(sentence), sentence[0])
    return ule1
