#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i in range(len(row)):
            print("{:d}".format(row[i]), end='')
            print("{}".format('' if i == (len(row) - 1) else ' '), end='')
        print()
