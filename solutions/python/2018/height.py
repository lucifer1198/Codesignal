"""
This is a reverse challenge, enjoy!
"""


def height(t):
    # by ernie_y
    A = numpy.tile(0, 2**17)
    for i in t[::-1]:
        A[:~i] += 1
        t[-A[0]] = A[~i]
    return t
