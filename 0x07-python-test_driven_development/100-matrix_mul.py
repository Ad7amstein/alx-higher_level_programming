#!/usr/bin/python3
"""Defines a matrix multiplication function.
"""


def matrix_mul(m_a, m_b):
    """Multiplies two matrices and returns the product.

    Args:
        m_a (list of lists): First matrix.
        m_b (list of lists): First matrix.

    Raises:
        TypeError: If m_a or m_b is not a list.
        TypeError: If m_a or m_b is not a list of lists.
        ValueError: If m_a or m_b is empty.
        TypeError: If one element of those list of lists
                   is not an integer or a float.
        TypeError: If m_a or m_b is not a rectangle.
        ValueError: If m_a and m_b can not be multiplied.
    Returns:
        The result of the multiplication.
    """
    """m_a and m_b must be a list first."""
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    """m_a and m_b must be a list of lists."""
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    """m_a and m_b can't be empty."""
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    """Each element in m_a and m_b must be integer or float."""
    if (not all(isinstance(num, int) or isinstance(num, float)
                for num in [num for row in m_a for num in row])):
        raise TypeError("m_a should contain only integers or floats")
    if (not all(isinstance(num, int) or isinstance(num, float)
                for num in [num for row in m_b for num in row])):
        raise TypeError("m_b should contain only integers or floats")

    """Each row in m_a and m_b must be the same size."""
    if not all(len(m_a[0]) == len(row) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(m_b[0]) == len(row) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    """The number of columns in m_a should be equal to the number
    of rows in m_b."""
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    new_matrix = []
    for i in range(len(m_a)):
        row = []
        for j in range(len(m_b[0])):
            x = 0
            for k in range(len(m_b)):
                x += m_a[i][k] * m_b[k][j]
            row.append(x)
        new_matrix.append(row)

    return new_matrix
