"""
Find the perimeter of a square with given sides.

Example

For n = 1, the output should be
squarePerimeter(n) = 4.
"""


def squarePerimeter(n):
    result = 0
    for i in range(4):
        result += n
    return result
