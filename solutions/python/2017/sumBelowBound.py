"""
Given an integer bound, find the maximal integer n such that 1 + 2 + ... + n ≤ bound.

Example

For bound = 14, the output should be
sumBelowBound(bound) = 4.
"""

# 61 chars
# def sumBelowBound(bound):
#  s = 0
#  i = 0
#  while s <= bound:
#    s += i
#    i += 1
#  return i - 2

# 50 chars
b, = eval(dir()[0])
s = 0
i = 0
while s <= b:
    s += i
    i += 1
return i - 2
