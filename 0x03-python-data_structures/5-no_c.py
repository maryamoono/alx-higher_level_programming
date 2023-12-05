def no_c(my_string):
    p = 0
    new_string = my_string[:]
    for z in range(len(my_string)):
        if my_string[z] == 'c' or my_string[z] == 'C':
            new_string = new_string[:(z - p)] + my_string[z+1:]
            p += 1
    return new_string
