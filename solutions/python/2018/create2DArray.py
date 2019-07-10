"""

Given array of integers lengths, create an array of arrays output such that output[i] consists of lengths[i] elements and output[i][j] = j.

Example

For lengths = [1, 2, 0, 4], the output should be

create2DArray(lengths) = [[0],
                          [0, 1],
                          [],
                          [0, 1, 2, 3]]
"""


def create2DArray(lengths):
    return [range(i) for i in lengths]
