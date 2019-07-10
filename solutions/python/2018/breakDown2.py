"""
You know the deal. :) If not, look at breakDown1. The goal this time is to calculate a few useful numbers.

Given an array of strings, output the following:
An array of various whole, positive numbers, as defined in the examples.

Example
For strings = ["2,3", "1,8", "3,11"], the output should be
breakDown2(strings) = [2, 1, 3, 264, 88, 33, 24].
Layout:
c misc b
"2 , 3"
"1 , 8"
"3 , 11"
Output:
[c1, c2, c3, B, B1, B2, B3],
Where B = b1 * b2 * b3
And B# = B / b# where # = 1, 2, or 3
So, the output is:
[2, 1, 3, 264, 88, 33, 24].
"""

a, b, c, d, e, f = map(int, re.findall('\d+', str(eval(dir()[0]))))
return a, c, e, b * d * f, d * f, b * f, b * d
