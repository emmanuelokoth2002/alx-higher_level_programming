#!/usr/bin/python3

"""Defines a matrix division function"""


def matrix_divided(matrix, div):
    """Check if matrix is a list of lists of integers or floats"""

    if not all(isinstance(row, list) and all(isinstance(elem, (int, float)) for elem in row) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    """Check if each row of the matrix has the same size"""
    row_size = len(matrix[0])
    if not all(len(row) == row_size for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    
    """Check if div is a number (integer or float)"""
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    
    """Check if div is not equal to zero"""
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    """Divide all elements of the matrix by div, rounded to 2 decimal places"""
    return [[round(elem/div, 2) for elem in row] for row in matrix]
