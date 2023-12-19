#!/usr/bin/python3
def magic_calculation(a, b):
    result = 0
    for v in range(1, 3):
        try:
            if (v > a):
                raise Exception("Too far")
            result += (a ** b) / v
        except Exception:
            result = b + a
            break
    return (result)
