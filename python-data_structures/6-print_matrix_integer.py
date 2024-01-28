#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    i = 0
    while i < len(matrix):
        j = 0
        while j < len(matrix[i]):
            print("{:d}".format(matrix[i][j]), end="")
            if j == (len(matrix[i]) - 1):
                print()
            else:
                print(" ", end="")
            j += 1
        i += 1
    if matrix == [[]]:
        print("")
