#!/usr/bin/python3
"""Defines a lazy matrix mul function."""
import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """Multiplies two matrices and returns the product.

    Args:
        m_a (list of lists): First matrix.
        m_b (list of lists): First matrix.
    Returns:
        The result of the multiplication.
    """
    return np.matmul(m_a, m_b)