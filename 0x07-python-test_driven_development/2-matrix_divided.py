#!/usr/bin/python3
""" This function divides the element of matrix and round it up to 2d.p """


def matrix_divided(matrix, div):
    """ It returns the division of element in matrix in 2 d.p """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(element, int) or isinstance(element, float))
                    for element in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    result_matrix = ([list(map(lambda x: round(x / div, 2), row))
                     for row in matrix])
    return result_matrix
