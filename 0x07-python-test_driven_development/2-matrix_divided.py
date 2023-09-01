#!/usr/bin/python3
"""Defines a matrix divided function."""


def matrix_divided(matrix, div):
    """Divides all the matrix elements by div

    Args:
        matrix (list[][] of int or float): Matrix to be divided
        div (int or float): Number to divide by

    Raises:
        TypeError: If any element of the matrix is not of type (int or float).
                   If all the rows doesn't have the same size.
                   If div not an (int or float).
        ZeroDivisionError: If div is equal to zero.

    Returns: The matrix after the division.
    """
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if not isinstance(matrix, list) or matrix == [] or \
            not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) \
                        of integers/floats")
    row_len = len(matrix[0])

    new_matrix = []
    for i in range(len(matrix)):
        if len(matrix[i]) != row_len:
            raise TypeError("Each row of the matrix must have the same size")
        new_matrix.append(list(matrix[i]))
        for j in range(len(matrix[i])):
            if not isinstance(matrix[i][j], int) and not isinstance(matrix[i][j], float):
                raise TypeError("matrix must be a matrix (list of lists) \
                                of integers/floats")
            new_matrix[i][j] = round(new_matrix[i][j] / div, 2)

    return new_matrix
