"""
Check if the given matrix is an identity matrix.

Example

For

matrix = [[1, 0, 0],
          [0, 1, 0],
          [0, 0, 1]]
the output should be
isIdentityMatrix(matrix) = true;

For

matrix = [[1, 0, 0],
          [0, 0, 0],
          [0, 0, 1]]

the output should be
isIdentityMatrix(matrix) = false.
"""


def isIdentityMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i == j and matrix[i][j] != 1:
                return False
            else:
                if i != j and matrix[i][j] != 0:
                    return False
    return True
