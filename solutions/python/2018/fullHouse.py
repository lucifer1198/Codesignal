"""
This is a reverse challenge, enjoy!

Sequence up to 15 for easier viewing:
[0, 1, 2, 3, 5, 9, 15, 26, 45, 78, 136, 238, 418, 737, 1304, 2315]

Hint:
FullHouse = A Set and a Pair.
Variable name = Fib.
Set Fib + Pair Fib = Full House.

Last Hint:
3 Fib + 2 Fib = Full House.
"""


def fullHouse(f):
    # by c_w
    a = x = 1
    b = y = z = 0
    while f:
        a, b = b, a + b
        x, y, z = y, z, x + y + z
        f -= 1
    return b + y
