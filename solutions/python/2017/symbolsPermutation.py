"""
Determine if it is possible to rearrange the characters in a string to obtain another string.

Example

For word1 = "abc" and word2 = "cab", the output should be
symbolsPermutation(word1, word2) = true;

For word1 = "aaaa" and word2 = "aaa", the output should be
symbolsPermutation(word1, word2) = false.
"""


def symbolsPermutation(word1, word2):
    chr1 = list(word1)
    chr1.sort()

    chr2 = list(word2)
    chr2.sort()

    return chr1 == chr2
