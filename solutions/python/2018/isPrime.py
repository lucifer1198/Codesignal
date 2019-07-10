"""
Implement a function that determines if a given positive integer is a prime or not.

Example

For n = 47, the output should be
isPrime(n) = true;

For n = 4, the output should be
isPrime(n) = false.
"""


def isPrime(n):
    divisor = 2
    while n > divisor:
        if n % divisor == 0:
            return False
        else:
            divisor = divisor + 1
    return True
