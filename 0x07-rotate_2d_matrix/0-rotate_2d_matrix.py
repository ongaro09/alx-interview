#!/usr/bin/python3
"""A script to rotate a 2D matrix"""


def rotate_2d_matrix(matrix):
    n = len(matrix)

    for layer in range(n // 2):
        first = layer
        last = n - 1 - layer
        for i in range(first, last):
            top = matrix[first][row]
            matrix[first][row] = matrix[last - row + first][first]
            matrix[last - row + first][first] = matrix[last][last - row + first]
            matrix[last][last - row + first] = matrix[row][last]
            matrix[row][last] = top
