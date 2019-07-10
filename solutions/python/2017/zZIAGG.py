"""
This is a reverse challenge, enjoy!

# n: 1
# [[1]]
#
# n: 2
# [[1,2],
#  [3,4]]
#
# n: 3
# [[1,2,6],
#  [3,5,7],
#  [4,8,9]]
"""


def zZIAGG(n):
    # solution by winstonsmith
    R = range(n)
    A = [(i, j) for i in R for j in R]
    A = sorted(A, key=lambda (y, z): (y + z, y if (y + z) % 2 else z))
    return [[1 + A.index((i, j)) for j in R] for i in R]
