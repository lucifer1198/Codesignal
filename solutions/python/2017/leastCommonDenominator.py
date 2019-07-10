"""
You need to sum up a bunch of fractions that have different denominators. In order to do this, you need to find the least common denominator of all the fractions. As a professional programmer, you know that the least common denominator is in fact their LCM.

Least common multiple (LCM) of numbers a and b is defined as the smallest number that is divisible by both a and b.

For the given list of denominators, find the least common denominator by finding their LCM.

Example

For denominators = [2, 3, 4, 5, 6], the output should be
leastCommonDenominator(denominators) = 60.
"""

from fractions import gcd
from functools import reduce


def leastCommonDenominator(denominators):
    return reduce(lambda x, y: (x * y) // gcd(x, y), denominators)
