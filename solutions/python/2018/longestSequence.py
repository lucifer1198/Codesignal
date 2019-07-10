"""
Given a sequence of integers find the length of its largest subsequence that forms an arithmetic progression.

Example

For a = [1, 7, 3, 5, 4, 2], the output should be
longestSequence(a) = 3.

Explanation: [1, 3, 5] is a subsequence that's also an arithmetic progression.
"""


def longestSequence(a):

    best = 1
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            diff = a[j] - a[i]
            if diff == 0:
                continue
            cur = 1
            last = a[i]
            for k in range(j, len(a)):
                if a[k] - last == diff:
                    cur += 1
                    last = a[k]
            if cur > best:
                best = cur

    return best
