#!/usr/bin/python3
def square_matrix_simple(matrix=[]):

    """
    Return a new matrix with each element squared.

    Args:
        matrix (list[list]): The input matrix.

    Returns:
        list[list]: The new matrix with squared elements.
    """
    new_matrix = matrix.copy()

    for i in range(len(matrix)):
        new_matrix[i] = list(map(lambda x: x**2, matrix[i]))

    return (new_matrix)
