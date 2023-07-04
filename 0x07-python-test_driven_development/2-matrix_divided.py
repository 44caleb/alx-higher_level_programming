#!/usr/bin/python3
"""function that divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """
    divides all the elements of a matrix
    Arg:
        matrix (array): array of lists
        div (int/float): divisor
    Returns:
        new matrix
    """
    m = 'matrix must be a matrix (list of lists) of integers/floats'
    m2 = 'Each row of the matrix must have the same size'
    m_size = len(matrix[0])

    for row in matrix:
        if len(row) != m_size:
            raise TypeError(m2)
        for column in row:
            if not isinstance(column, (float, int)):
                raise TypeError(m)
    if not isinstance(div, (float, int)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    new_matrix = [[round(x/div, 2) for x in y] for y in matrix]
    return new_matrix
