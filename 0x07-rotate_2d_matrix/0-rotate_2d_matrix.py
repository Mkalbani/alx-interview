#!/usr/bin/python3
"""
0x07 - Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """
    Rotates an nxn 2D matrix 90 degrees clockwise in place

    :param matrix: List of lists
    """
    n = len(matrix)

    # Step 1: Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: Reverse each row
    for row in matrix:
        row.reverse()
