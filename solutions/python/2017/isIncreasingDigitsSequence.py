def isIncreasingDigitsSequence(n):
    s = str(n)
    for i in range(len(s)-1):
        if s[i] >= s[i+1]:
            return False
    return True

"""
Call an integer an increasing digits sequence if its digits considered from left to right form a strictly increasing sequence.

Given an integer, check if it is an increasing digits sequence.

Example

For n = 12345, the output should be
isIncreasingDigitsSequence(n) = true;
For n = 2446, the output should be
isIncreasingDigitsSequence(n) = false;
For n = 543, the output should be
isIncreasingDigitsSequence(n) = false.
"""
