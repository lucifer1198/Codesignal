"""
Pinocchio's father wants to remake a new nose for Pinocchio.
He has N wood bars, wood bar i have length bars[i].
As a mathematical lover, he offers the following algorithm to get the length of the wood bar needed:

If remaining only one wood bar, he will take it to make Pinocchio's nose.
If there is more than one wood bar, he will do the following:

Step 1: Choose the wood bar i with the smallest length bars[i], then select the wood bar j with the smallest length bars[j] in the remaining bars.
Step 2: If bars[i] = bars[j], throw away a bar, go back to Step 1.
Step 3: If bars[i] < bars[j], cut off bars[j] a segment equals bars[i], go back to Step 1.

Calculate the length of the wood bar remaining that he get.

Example
For bars = [4, 5, 6], the output should be
woodBars(bars) = 1.
"""

# solution by sifulan
# 81 chars
# def woodBars(bars):
#    m = min(bars)
#    a = [x%m for x in bars]
#    a.append(m)
#    return min(i for i in a if i > 0)

# 67 chars
# b, = eval(dir()[0])
# m  = min(b)
# a  = [x%m for x in b] + [m]
# return min(i for i in a if i > 0)

# 64 chars
b, = eval(dir()[0])
m = min(b)
return min(i for i in [x % m for x in b] + [m] if i > 0)
