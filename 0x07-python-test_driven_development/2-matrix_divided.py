#!/usr/bin/python3
"""
A module that defines function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix.
    Args:
        matrix: a matrix that is a list of lists of integers or floats
        div: the divisor
    Return:
        a new matrix
    Raises:
        TypeError: if matrix is not a list of lists of integers or floats.
        TypeError: if each row of the matrix is not of the same size
        TypeError: if div is not a number (integer or float)
        ZeroDivisionError: if div is equal to 0
    """
    string = "matrix must be a matrix (list of lists) of integers/floats"

    if matrix == []:
        raise TypeError(string)
    if not isinstance(matrix, list):
        raise TypeError(string)
    if not all(isinstance(element, (int, float)) and not
       isinstance(element, bool) for row in matrix for element in row):
        raise TypeError(string)

    if not matrix or not matrix[0]:
        raise TypeError(string)

    check_length = len(matrix[0])
    if any(len(row) != check_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)) or isinstance(div, bool):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new = [list(round(element / div, 2) for element in row) for row in matrix]
    return new
