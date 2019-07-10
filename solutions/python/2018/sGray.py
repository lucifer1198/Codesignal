"""
The area of square is area.
shade
How much is the gray area and double perimeter?

Example
For area = 4, the output should be
sGray(area) = [1.260587, 8.37758].
"""

# by e--
# c = math.acos(.5)
# v = c - math.sin(2*c)/2
# x+2*y=a-pi*r*r/4
# a*v=z+y+2*x
# [(1-pi-4*v)*a , 4*c*a**.5]
# [.3151467436277211*a,4.188790204786391*a**.5]
sGray = lambda a: [.31514674363 * a, 4.1887902 * a**.5]
