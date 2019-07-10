"""
Given integers n, l and r, find the number of ways to represent n as a sum of two integers A and B such that l ≤ A ≤ B ≤ r.

Example

For n = 6, l = 2 and r = 4, the output should be

countSumOfTwoRepresentations3(n, l, r) = 2.

These ways are: 2 + 4 = 6 and 3 + 3 = 6.
"""


def countSumOfTwoRepresentations3(n, l, r):
    result = 0
    i = 1
    while (i <= n - i):
        if (l <= i and n - i <= r):
            result = result + 1
        i = i + 1
    return result
