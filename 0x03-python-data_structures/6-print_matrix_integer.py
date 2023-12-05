#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for z in range(len(matrix)):
            p = 0
            for p in range(len(matrix[z])):
                if p == len(matrix[z]) - 1:
                    print("{:d}".format(matrix[z][p]), end='')
                else:
                    print("{:d} ".format(matrix[z][p]), end='')
            print()
