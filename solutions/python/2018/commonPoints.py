"""
Given integers l1, r1, l2 and r2, count integers x such that l1 < x < r1 and l2 < x < r2.

Example

For l1 = 1, r1 = 5, l2 = 2 and r2 = 10, the output should be
commonPoints(l1, r1, l2, r2) = 2.
"""

# 74 chars
# def commonPoints(l1, r1, l2, r2):
#    r = min(r1, r2) - max(l1, l2) - 1
#    if r < 0:
#        return 0
#    return r


# 60 chars
a, b, c, d = eval(dir()[0])
r = min(b, d) - max(a, c) - 1
return 0 if r < 0 else r
