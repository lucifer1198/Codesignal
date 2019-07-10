"""
In this challenge you'll be finding the smallest multiple of any integer element in a given array,
and is the nth multiple of the number.

Example
For array = [4, 10, 2] and nth = 4, the output should be findSmallestMultipleInArray(array, nth) = 8.
The 4th smallest multiple (8) of any number in the array is 2.
"""

# def findNthSmallestMultipleInArray(array, nth):
#    return min(n * nth for n in array)

a, t = eval(dir()[0])
return min(n * t for n in a)
