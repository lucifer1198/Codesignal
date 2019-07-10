"""
Given a sentence, check whether it is a pangram or not.

Example

For sentence = "The quick brown fox jumps over the lazy dog.", the output should be
isPangram(sentence) = true;
For sentence = "abcdefghijklmnopqrstuvwxya", the output should be
isPangram(sentence) = false.
"""


def isPangram(sentence):
    found = []
    result = True
    for i in range(26):
        found.append(False)
    for i in range(len(sentence)):
        code = ord(sentence[i])
        if ord('A') <= code and code <= ord('Z'):
            code += ord('a') - ord('A')
        if ord('a') <= code and code <= ord('z'):
            found[code - ord('a')] = True

    for i in range(26):
        if not found[i]:
            result = False

    return result


# isPangram = lambda s: not set(string.ascii_lowercase) - set(s.lower())

isPangram = lambda s: {*string.ascii_lowercase} <= {*s.lower()}
