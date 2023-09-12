#!/usr/bin/python3
"""Defines a pascal triangle function."""


def pascal_triangle(n):
    """Returns a list of lists of integers
    representing the Pascal's triangle of n."""
    if n <= 0:
        return []
    pascal = []
    for i in range(n):
        pascal.append([])
        for j in range(i + 1):
            if j in [0, i]:
                pascal[i].append(1)
            else:
                pascal[i].append(pascal[i - 1][j - 1] + pascal[i - 1][j])

    return pascal
