#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = my_list.copy()
    for z in range(len(new_list)):
        if new_list[z] % 2 == 0:
            new_list[z] = True
        else:
            new_list[z] = False
    return new_list
