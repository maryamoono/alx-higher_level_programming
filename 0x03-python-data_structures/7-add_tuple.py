#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    len_a = len(tuple_a)
    len_b = len(tuple_b)

    if len_a == 0:
        c1 = 0
        c2 = 0
    elif len_a == 1:
        c1 = tuple_a[0]
        c2 = 0
    else:
        c1 = tuple_a[0]
        c2 = tuple_a[1]

    if len_b == 0:
        d1 = 0
        d2 = 0
    elif len_b == 1:
        d1 = tuple_b[0]
        d2 = 0
    else:
        d1 = tuple_b[0]
        d2 = tuple_b[1]

    new_tuple = (c1 + d1, c2 + d2)

    return (new_tuple)
