#!/usr/bin/python3
def make_square(n):
    return n * n


def square_matrix_simple(matrix=[]):
    sqr_matrix = []
    for row in matrix:
        new_row = list(map(make_square, row))
        sqr_matrix.append(new_row)
    return sqr_matrix
