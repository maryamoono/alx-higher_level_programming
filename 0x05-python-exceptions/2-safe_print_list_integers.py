#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    num = 0
    for v in range(x):
        try:
            print("{:d}".format(my_list[v]), end='')
        except (ValueError, TypeError):
            pass
        else:
            num += 1
    print()
    return num
