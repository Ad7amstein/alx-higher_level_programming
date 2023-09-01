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
    if (not isinstance(matrix, list) or matrix == [] or
        not all(isinstance(row, list) for row in matrix) or
        not all(isinstance(num, int) or isinstance(num, float)
                for num in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) \
                        of integers/floats")

    row_len = len(matrix[0])
    if (not all(len(row) == row_len for row in matrix)):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return (list(map(lambda row: list(map(lambda x: round(x / div, 2), row)),
                     matrix)))
