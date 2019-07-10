"""
Given array of integers, find the maximal possible sum of some of its k consecutive elements.

Example

For inputArray = [2, 3, 5, 1, 6] and k = 2, the output should be
arrayMaxConsecutiveSum(inputArray, k) = 8.

All possible sums of 2 consecutive elements are:

2 + 3 = 5;
3 + 5 = 8;
5 + 1 = 6;
1 + 6 = 7.
Thus, the answer is 8.
"""


def arrayMaxConsecutiveSum(inputArray, k):

    result = 0
    currentSum = 0

    for i in range(k - 1):
        currentSum += inputArray[i]
    for i in range(k - 1, len(inputArray)):
        currentSum += inputArray[i]
        if currentSum > result:
            result = currentSum
        currentSum -= inputArray[i - k + 1]

    return result
