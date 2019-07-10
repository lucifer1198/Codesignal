"""
You were rummaging around your closet looking for pants when you fell into a time warp.
Now you are back in highschool! You have to do your homework (again). Luckily, you know how to do this stuff!

At the time, you were taking Algebra. You are too lazy to do the work out a second time, so you write a program to do it for you.
Your assignment is simple. You are working with quadratics and must solve for "x".

Given an array coefficients, return an array of answers in increasing order, rounded to the nearest hundredths place.

Example
For coefficients = [1, -4, 4], the output should be
highschoolThrowback(coefficients) = [2].
"""

# solution by sifulan

# 135 chars
# import numpy as np
#
# def highschoolThrowback(coefficients):
#    roots = list(set(round(n, 2) for n in np.roots(coefficients).tolist()))
#    return sorted(roots)


# 100 chars
# import numpy as N
# def highschoolThrowback(c):
#    return sorted(list(set(round(n, 2) for n in N.roots(c).tolist())))


# 85 chars
# c, = eval(dir()[0])
# import numpy as N
# return sorted(set(round(n, 2) for n in N.roots(c).tolist()))


# 82 chars
c, = eval(dir()[0])
import numpy as N
return sorted(set(round(n, 2) for n in list(N.roots(c))))
