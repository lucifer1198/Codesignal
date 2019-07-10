"""
Compare two integers given as strings.

Example

For a = "12" and b = "13", the output should be
compareIntegers(a, b) = "less";
For a = "875" and b = "799", the output should be
compareIntegers(a, b) = "greater";
For a = "1000" and b = "1000", the output should be
compareIntegers(a, b) = "equal".
"""


def compareIntegers(a, b):

    if len(a) > len(b):
        return 'greater'
    if len(a) < len(b):
        return 'less'
    if a < b:
        return 'less'
    if a > b:
        return 'greater'
    return 'equal'


def compareIntegers(a, b):
    a = int(a)
    b = int(b)
    return 'less' if a < b else 'equal' if a == b else 'greater'
