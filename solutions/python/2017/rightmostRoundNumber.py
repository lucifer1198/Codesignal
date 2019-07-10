"""
Given an array of integers, find the rightmost round number in it and output its position in the array (0-based).
If there are no round numbers in the given array, output -1.

round number: An integer is called a round number if it ends with one or more zeroes.

Example

For inputArray = [0, 5, 10, 15], the output should be
rightmostRoundNumber(inputArray) = 2;
For inputArray = [1, 2, 3, 4, 5], the output should be
rightmostRoundNumber(inputArray) = -1.
"""


def rightmostRoundNumber(a):
    x = 0
    n = 0
    f = False
    while x < len(a):
        if a[x] % 10 == 0:
            n = x
            f = True
        x += 1
    if f:
        return n
    return -1
