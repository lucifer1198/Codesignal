"""
Given integers l and r, find the number of different pairs of integers A and B such that l <= A <= r and l <= B <= r and A3 = B2.

Note that A and B may even coincide (A = B = 1 is one of the possibilities).

Example

For l = 1 and r = 4, the output should be
equationSolutions(l, r) = 1.

There is only one solution: (1, 1).

For l = 1 and r = 8, the output should be
equationSolutions(l, r) = 2.

There are two solutions: (1, 1) and (4, 8).
"""

# solution by: Pedro_O
def equationSolutions(l, r):
    ct = 0
    for a in xrange(l, r+1):
        for b in xrange(l, r+1):
            if a**3 == b**2:
                ct += 1
    return ct
