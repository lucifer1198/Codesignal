"""
Construct an array b of [prefix sums] of the given array a.

Array of prefix sums is defined as:

  B[0] = A[0]
  B[1] = A[0] + A[1]
  B[2] = A[0] + A[1] + A[2]
  ...
  B[n - 1] = A[0] + A[1] + ... + A[n - 1]

b is defined as:

  b[0]   = a[0]
  b[1]   = a[0] + a[1]
  b[2]   = a[0] + a[1] + a[2]
  ...
  b[n - 1] = a[0] + a[1] + ... + a[n - 1]
where n is the length of a.

Example

For a = [1, 2, 3], the output should be
prefixSums(a) = [1, 3, 6].

b would be equal to [1, 1 + 2, 1 + 2 + 3] = [1, 3, 6]
"""


def prefixSums(a, *A):
    # solution by ernie_y
    s = 0
    for i in a:
        s += i
        A += s,
    return A
