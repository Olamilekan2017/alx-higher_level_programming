#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix:
        new = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        for r in range(len(matrix)):
            for i in range(len(matrix[0])):
                new[r][i] = matrix[r][i] ** 2
        return new
