"""
You're given a substring s of some cyclic string.
What's the length of the smallest possible string that can be concatenated to itself many times to obtain this cyclic string?

Example

For s = "cabca", the output should be
cyclicString(s) = 3.

"cabca" is a substring of a cycle string "abcabcabcabc..." that can be obtained by concatenating "abc" to itself.
Thus, the answer is 3.
"""


def cyclicString(s1):

    for answer in range(1, len(s1)):
        correct = True
        for position in range(answer, len(s1)):
            if s1[position] != s1[position - answer]:
                correct = False
        if correct:
            return answer
    return len(s1)
