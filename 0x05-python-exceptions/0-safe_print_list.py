#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        num = 0
        for v in range(x):
            print(my_list[v], end='')
            num += 1
    except IndexError:
        None
    finally:
        print()
    return num
