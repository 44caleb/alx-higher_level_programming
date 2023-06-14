#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    n_matrix = [[x * x for x in row] for row in matrix]
    return n_matrix
