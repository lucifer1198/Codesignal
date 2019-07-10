# Question: https://python.web.id/blog/differentsymbolsnaive-cf/

"""
Given a string, find the number of different characters in it.

Example

For s = "cabca", the output should be
differentSymbolsNaive(s) = 3.

There are 3 different characters a, b and c.
"""


def differentSymbolsNaive(s):
    result = 0
    for i in range(26):
        found = False
        j = 0
        while j < len(s):
            if ord(s[j]) == ord('a') + i:
                found = True
            j += 1
        if found:
            result += 1
    return result


def differentSymbolsNaive(s):
    return len(list(set(list(s))))
