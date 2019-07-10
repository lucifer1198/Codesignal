"""
Let A = a^(b^(c^d)) and B = x^(y^(z^t)).
You have to compare A and B.

Input an array m with length 8.
m[0] = a, m[1] = b, m[2] = c, m[3] = d, m[4] = x, m[5] = y, m[6] = z and m[7] = t.
If A > B, return 1.
If A == B, return 0.
If A < B, return -1.

Example

For m = [2, 5, 2, 5, 5, 2, 5, 2], the output should be compare2Power(m) = 1.
It means 2^(5^(2^5)) > 5^(2^(5^2)).
"""

# solution by sifulan
# 109 chars
# def compare2Power(m):
#    A = m[0]^(m[1]^(m[2]**m[3]))
#    B = m[4]^(m[5]^(m[6]**m[7]))
#    if A > B:
#        return 1
#    elif A == B:
#        return 0
#    return -1

# 98 chars
m, = eval(dir()[0])
A = m[0] ^ (m[1] ^ (m[2]**m[3]))
B = m[4] ^ (m[5] ^ (m[6]**m[7]))
return 1 if A > B else 0 if A == B else -1
