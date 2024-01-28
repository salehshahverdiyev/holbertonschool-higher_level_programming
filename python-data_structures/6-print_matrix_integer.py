#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    i = 0
    while i < len(matrix):
        j = 0
        while j < len(matrix[0]):
            print("{:d}".format(matrix[i][j]), end=(" " if j < len(matrix[0]) - 1 else "\n"))
            j += 1
        i += 1
