#!/usr/bin/python3
""" Defines a matrix multiplication function using NumPy. """
import numpy as npy


def lazy_matrix_mul(m_a, m_b):
    """ Return the multiplication of two matrices. """

    return (npy.matmul(m_a, m_b))
