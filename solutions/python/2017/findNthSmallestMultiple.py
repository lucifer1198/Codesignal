"""
In this challenge, you'll be finding the nth smallest multiple of any integer element in a given array, a.

This challenge is inspired by my original interpretation of a previous challenge.
https://codefights.com/challenge/GrnTbWrj62B6AJXag

Example
For a = [3, 5, 7] and n = 7, the output should be findNthSmallestMultiple(a, n) = 12.

The list of multiples is:
[3, 5, 6, 7, 9, 10, 12, 14, 15 ... ]

and the 7th multiple is 12.
"""

# solution by sifulan
# def findNthSmallestMultiple(a, n):
#    return sorted(set(x*y for x in a for y in range(n)))[n]

a, n = eval(dir()[0])
return sorted(set(x * y for x in a for y in range(n)))[n]
