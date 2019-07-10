"""
We call an element of an array its peak if the array is strictly increasing on the left side of the peak and strictly decreasing on its right side.
So if we have an array called sequence of length n, sequence[k] is a peak if and only if

sequence[0] < sequence[1] < ... < sequence[k]

and

sequence[k] > sequence[k + 1] > ... > sequence[n - 1]

Knowing that sequence definitely has a peak and that the peak is not its first or last element, find the peak's value.

Example

For sequence = [1, 2, 4, 7, 9, 3, -2, -10], the output should be
sequencePeakElement(sequence) = 9.
"""

def sequencePeakElement(sequence):
    left = 1
    right = len(sequence) - 2
    while left < right:
        middle = (left + right) // 2
        if sequence[middle] > max(sequence[middle - 1], sequence[middle + 1]):
            left = right = middle
            break
        if sequence[middle - 1] < sequence[middle]:
            left = middle + 1
        else:
            right = middle - 1
    return sequence[left]
