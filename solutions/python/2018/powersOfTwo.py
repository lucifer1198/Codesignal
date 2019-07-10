"""
Every positive integer can be uniquely represented as a sum of different positive powers of two.

Given a number n, return a sorted array of different powers of two that sum up to n.

Example

For n = 5, the output should be
powersOfTwo(n) = [1, 4].
"""


def powersOfTwo(n):
    a = []
    c = 1
    while n > 0:
        if n % 2 == 1:
            a.append(c)
        n >>= 1
        c <<= 1
    return a
