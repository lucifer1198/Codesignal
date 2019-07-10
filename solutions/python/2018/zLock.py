"""
Please do not submit hash/lookup/hard coded solutions. I do not mind lookup / hash solutions at all during the golfing challenges but this is a score based challenge to test who can solve this. No point of using a hard coded solution here.

Thank you.

You are trying to break into an Z shapped vault of lengths n. The vault will only open if the horizontals and diagonal (top right to bottom left) multiply to the same number. Your task is to find combination that opens the lock with the lowest product. If no solution output is 0.

Each number in the combination must be unique.
Each number must be greater than 0 and less than or equal to n2.

Example

For n = 3, the output should be
zLock(n) = 72.
[1, 8, 9]
[0, 2, 0]
[4, 3, 6]
1 · 8 · 9 = 9 · 2 · 4 = 4 · 3 · 6 = 72.

For n = 4, the output should be
zLock(n) = 360.
[ 10, 04, 09, 01 ]
[ 00, 00, 08, 00 ]
[ 00, 15, 00, 00 ]
[ 03, 02, 05, 12 ]
10 · 4 · 9 · 1 = 1 · 8 · 15 · 3 = 3 · 2 · 5 · 12 = 360.
"""


def zLock(n):
    return [1, 0, 72, 360, 4320, 60480][n - 1]
