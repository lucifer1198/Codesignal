"""
For given integers a and b, find the last digit of ab.

Example

For a = 2 and b = 5, the output should be
lastDigit(a, b) = 2.

Explanation: 25 = 32.
"""


def lastDigit(a, b):
    return pow(a, b, 10)
