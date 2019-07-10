"""

Determine if it is possible to sort an array by reversing one of its contiguous subarrays.

It's guaranteed that array is not initially sorted.

Example

For inputArray = [-1, 5, 4, 3, 2, 8], the output should be
reverseToSort(inputArray) = true.

We can reverse [5, 4, 3, 2] to make it sorted.

For inputArray = [1, 3, 2, 5, 4, 6], the output should be
reverseToSort(inputArray) = false.
"""


def reverseToSort(inputArray):
    for a in range(len(inputArray) - 1):
        for b in range(a + 1, len(inputArray) + 1):
            window = inputArray[a:b]
            if sorted(inputArray) == inputArray[:a] + window[::-1] + inputArray[b:]:
                return len(set(inputArray)) == len(inputArray)
    return False
