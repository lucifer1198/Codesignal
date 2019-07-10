"""

Given a string, find the shortest possible string which can be achieved
by adding characters to the end of initial string to make it a palindrome.

Example

For st = "abcdc", the output should be
buildPalindrome(st) = "abcdcba".
"""


def buildPalindrome(s):
    if s == s[::-1]:
        return s
    d = []
    for i in range(len(s)):
        r = s + s[::-1][i:]
        if r == r[::-1]:
            d += [r]
    return sorted(d, key=len)[0]
