"""
You have an array a of different integers which you want to sort.
However, you are not interested in the sorted array itself, but in the positions the elements in it used to have in a.
Thus your task is to return an array of indices the elements in the sorted array a used to have before sorting.

Example

For a = [7, 4, 1], the output should be
sortedIndices(a) = [2, 1, 0].

Sorted a would be [1, 4, 7], which is [a[2], a[1], a[0]] = [a[indices[0]], a[indices[1]], a[indices[2]]]).
So, the answer is indices = [2, 1, 0].

For a = [1, 2, 3, 5, 8], the output should be
sortedIndices(a) = [0, 1, 2, 3, 4];

For a = [5, 3, 4, 1, 2], the output should be
sortedIndices(a) = [3, 4, 1, 2, 0].
"""


def sortedIndices(a):
    indices = []
    for i in range(len(a)):
        indices.append(i)
    for i in range(len(a) - 1):
        for j in range(len(a) - i - 1):
            if a[indices[j]] > a[indices[j + 1]]:
                tmp = indices[j + 1]
                indices[j + 1] = indices[j]
                indices[j] = tmp
    return indices
