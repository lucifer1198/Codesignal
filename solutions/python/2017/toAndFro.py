"""
A person is moving along a straight line. Initially he is at point A. He goes to point B from A with speed equal to 1 meter per second.
Immediately after reaching B he turns around and heads to A from B with the same speed. After reaching point A he turns around once again and heads to B. etc.
We need an algorithm that identifies the location of the person at any given moment in time.

It's guaranteed that A and B are two different points.

Example

For a = 2, b = 4 and t = 3, the output should be
toAndFro(a, b, t) = 3.
"""

# solution by sifulan
# def toAndFro(a, b, t):
#    l = abs(a-b)
#    t %= (2 * l)
#
#    if t <= l:
#        return a + (b-a) / abs(b-a) * t
#    else:
#        t -= l
#        return b + (a-b) / abs(a-b) * t

a, b, t = eval(dir()[0])
A = abs

l = A(a - b)
t %= 2 * l

if t <= l:
    return a + (b - a) / A(b - a) * t

t -= l
return b + (a - b) / A(a - b) * t
