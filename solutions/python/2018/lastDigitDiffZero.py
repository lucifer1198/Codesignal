"""
Find the last digit of n!(factorial), which is different from zero.

Example

For n = 5, the output should be
lastDigitDiffZero(n) = 2.
5! = 1 · 2 · 3 · 4 · 5 = 120.

For n = 6, the output should be
lastDigitDiffZero(n) = 2.
6! =1 · 2 · 3 · 4 · 5 · 6 = 720.

For n = 10, the output should be
lastDigitDiffZero(n) = 8.
10! = 3628800.
"""

n, = eval(dir()[0])
N = 1

while n:
    N *= n
    n -= 1

    while not N % 10:
        N //= 10
    N %= 10000

return N % 10
