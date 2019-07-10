"""
Find the number of elements that are contained in both of the given arrays.

Example

For a = [1, 2, 3] and b = [3, 4, 5], the output should be
sameElementsNaive(a, b) = 1.
"""


def sameElementsNaive(a, b):
    r = 0
    for i in a:
        if i in b:
            r += 1
    return r
