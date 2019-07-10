"""
Given integers x and n, find the largest integer k such that x0+x1+x2+...+xk ≤ n.

Example

For x = 2 and n = 5, the output should be
specialPolynomial(x, n) = 1.

We have 20 + 21 < 5 and 20 + 21 + 22 > 5.
"""


def specialPolynomial(x, n):
    s = 0
    for k in range(1000):
        s += math.pow(x, k)
        if s > n:
            return k - 1
