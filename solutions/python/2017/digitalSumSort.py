"""
You are given an array of integers. Sort it in such a way that if a comes before b then the sum of digits of a is less than or equal to the sum of digits of b.
If two numbers have the same sum of digits, the smaller one (in the regular sense) should come first.
For example 4 and 13 have the same sum of digits, however 4 < 13 thus 4 comes before 13 in any digitalSum sorting where both are present.

Example

For a = [13, 20, 7, 4], the output should be
digitalSumSort(a) = [20, 4, 13, 7].
"""


def digitalSumSort(a):

    def sumDigit(n):
        dValue = 0
        while n > 0:
            dValue += n % 10
            n //= 10
        return dValue

    bucks = dict()
    for i in range(len(a)):
        dValue = sumDigit(a[i])
        if dValue not in bucks:
            bucks[dValue] = []
        bucks[dValue].append(a[i])

    b = []
    for dValue in sorted(bucks):
        bucket = bucks[dValue]
        bucket.sort()
        for i in range(len(bucket)):
            b.append(bucket[i])

    return b


def digitalSumSort(a):
    b = [sum([int(x) for x in str(A)]) for A in a]
    return [x for _, x in sorted(zip(b, a))]
