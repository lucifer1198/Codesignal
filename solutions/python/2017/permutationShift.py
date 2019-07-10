"""
Define the permutation element shift as the difference between the element's value and its index.
For example, for permutation [1, 0, 2, 3] of array [0, 1, 2, 3] shifts for the respective elements are [1, -1, 0, 0].

Define the permutation shift as the difference between the maximal and the minimal element shifts among all of the permutation elements.

Given a permutation of integers from 0 to n - 1 for some integer n, find its shift.

Example

For permutation = [1, 0, 2, 3], the output should be
permutationShift(permutation) = 2.
"""

# by sifulan
# 108 chars
# def permutationShift(permutation):
#    out = []
#    for k, v in enumerate(permutation):
#        out.append(v-k)
#    return max(out) - min(out)

# 74 chars
# p, = eval(dir()[0])
# o = []
# for k, v in enumerate(p):
#    o.append(v-k)
# return max(o) - min(o)

# 73 chars
o = []
for k, v in enumerate(eval(dir()[0])[0]):
    o.append(v - k)
return max(o) - min(o)
