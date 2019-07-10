"""
Find the number of fixed points in a permutation of [1, 2, 3, ..., n] for some n.
Fixes points: A fixed point of a permutation p consisting of integers from 1 to n is such a number i (1 ≤ i ≤ n) that p[i] = i.

Example

For permutation = [1, 3, 2, 4, 5, 6], the output should be
fixedPointsPermutation(permutation) = 4.

The answer is 4 since 1, 4, 5 and 6 stayed in the same positions.
"""

def fixedPointsPermutation(permutation):
    result = 0
    for k, v in enumerate(permutation):
        if permutation[k] == k+1:
            result += 1
    return result

