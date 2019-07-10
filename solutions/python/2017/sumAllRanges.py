"""
Given an array array of positive integers, calculate the sum over the closed ranges defined by all the possible pairs in array.
Since this sum can be very large, return it modulo 109 + 7.

Example

For array = [1, 5, 2], the output should be
sumAllRanges(array) = 32.

We can define the following valid ranges: [1, 5], [1, 2], [2, 5].
The sum over all those ranges is sum([1..5]) + sum([1..2]) + sum([2..5]) = (1 + 2 + 3 + 4 + 5) + (1 + 2) + (2 + 3 + 4 + 5) = 32.

For array = [4, 2, 4, 3], the output should be
sumAllRanges(array) = 41.
The solution is sum([2..3]) + sum([2..4]) + sum([2..4]) + sum([3..4]) + sum([3..4]) + sum([4..4]) = 41.
"""

# solution by davefnbuck

# 85 chars
# def sumAllRanges(a):
#     i = s = t = 0
#     for n in sorted(a):
#         s += n*-~n*i - t
#         t += n*n-n
#         i += 1
#     return s/2 % (10**9+7)

# 84 chars
# def sumAllRanges(a):
#     i = s = t = 0
#     for n in sorted(a):
#         s -= ~n*n*i + t
#         t += ~-n*n
#         i += 1
#     return s/2 % (10**9+7)

# 83 chars
# def sumAllRanges(a):
#     s = t = 0
#     for n in sorted(a):
#         s -= ~n*n*~-len(a)/2 + t
#         t += n*n
#     return s % (10**9+7)

# 81 chars
a, = eval(dir()[0])
s = t = 0
for n in sorted(a):
    s -= ~n * n * ~-len(a) / 2 + t
    t += n * n
return s % (10**9 + 7)
