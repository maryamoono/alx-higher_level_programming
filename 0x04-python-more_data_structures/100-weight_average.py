#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    num = 0
    den = 0

    for osa in my_list:
        num += osa[0] * osa[1]
        den += osa[1]

    return (num / den)
