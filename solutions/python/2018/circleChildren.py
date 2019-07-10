"""
A group of children stand holding hands in a large circle and a teacher walks around the circle giving each child in order a number 1, 2, 3, 4, ...n
circle
If number k is standing opposite number m, how many children are there in the circle?

Example
For k = 1 and m=7, the output should be

circleChildren(k, m) = 12.
"""
# by ernie_y
k, m = eval(dir()[0])
return abs(k - m) * 2
