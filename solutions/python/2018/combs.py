"""
Miss X has only two combs in her possession, both of which are old and miss a tooth or two.
She also has many purses of different length, in which she carries the combs.
The only way they fit is horizontally and without overlapping.
Given teeth' positions on both combs, find the minimum length of the purse she needs to take them with her.

It is guaranteed that there is at least one tooth at each end of the comb.
It is also guaranteed that the total length of two strings is smaller than 32.
Note, that the combs can not be rotated/reversed.

Example

For comb1 = "*..*" and comb2 = "*.*", the output should be
combs(comb1, comb2) = 5.

Although it is possible to place the combs like on the first picture, the best way to do this is either picture 2 or picture 3.

https://codefightsuserpics.s3.amazonaws.com/tasks/combs/img/cbs.png
"""


def combs(comb1, comb2):

    def getMask(comb):
        mask = 0
        for i in range(0, len(comb)):
            c = comb[i]
            mask = (mask << 1) + (c == '*')
        return mask

    m1 = getMask(comb1)
    m2 = getMask(comb2)
    len1 = len(comb1)
    len2 = len(comb2)
    answer = len1 + len2
    for i in range(-len1, len2 + 1):
        if i < 0:
            tmp = m2 << (-i) & m1
            length = max(-i + len2, len1)
        else:
            tmp = m1 << i & m2
            length = max(i + len1, len2)
        if tmp == 0 and answer > length:
            answer = length

    return answer
