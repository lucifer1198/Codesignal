# -*- coding: utf-8 -*-

def extraNumber(A, B, C):
    if A == B: return C
    elif A == C: return B
    else: return A

extraNumber = lambda A, B, C: C if (A == B) else B if (A == C) else A

"""
Given three integers, two of them are guaranteed to be equal, find the third one.

Example

For A = 2, B = 4 and C = 2, the output should be
extraNumber(A, B, C) = 4.

Input/Output

[time limit] 4000ms (py)
[input] integer A

Constraints:
1 ≤ A ≤ 10^9.

[input] integer B

Constraints:
1 ≤ B ≤ 10^9.

[input] integer C

Constraints:
1 ≤ C ≤ 10^9.

[output] integer
"""
