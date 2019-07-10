"""
Check if the given matrix is lower triangular.

Example

For

matrix = [[1, 0, 0],
          [4, 0, 0],
          [0, 3, 3]]
the output should be
isLowerTriangularMatrix(matrix) = true;

For

matrix = [[1, 0, 1],
          [0, 5, 0],
          [2, 0, 3]]
the output should be
isLowerTriangularMatrix(matrix) = false.
"""


def isLowerTriangularMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if j > i and matrix[i][j] != 0:
                return False
    return True
