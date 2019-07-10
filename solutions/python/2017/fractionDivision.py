"""
Implement a function that can divide two fractions and produce a reduced fraction.

We call a fraction reduced if its numerator and denominator are relatively prime.

Two integers are said to be relatively prime (or coprime) if the only positive integer that evenly divides both of them is 1.

Example

For a = [2, 3] and b = [5, 6], the output should be
fractionDivision(a, b) = [4, 5].
"""


def fractionDivision(a, b):

    def gcdEuclid(a, b):
        if a == 0:
            return b
        return gcdEuclid(b % a, a)

    c = [a[0] * b[1], a[1] * b[0]]
    gcd = gcdEuclid(c[0], c[1])

    c[0] /= gcd
    c[1] /= gcd

    return c
