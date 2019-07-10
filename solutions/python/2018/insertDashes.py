"""
Transform a given sentence into a new one with dashes between each two consecutive letters.

Example

For inputString = "aba caba", the output should be
insertDashes(inputString) = "a-b-a c-a-b-a".
"""


def insertDashes(inputString):
    words = inputString.split(' ')
    for i in range(len(words)):
        words[i] = '-'.join(list(words[i]))
    return ' '.join(words)
