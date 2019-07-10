"""
Given an array of integers, we need to fill in the "holes" such that it contains all the integers from some range.

Example

For sequence = [6, 2, 3, 8], the output should be
makeArrayConsecutive(sequence) = [4, 5, 7].
"""


def makeArrayConsecutive(sequence):
    s = sorted(sequence)
    x = range(min(s), max(s) + 1)
    res = []
    for elem in x:
        if elem not in s:
            res.append(elem)
    return res
