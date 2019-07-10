"""
Given a string s containing only open and close parenthesis.
What is the minimum number of parenthesis that needs to be flipped for the string to become a set of balanced parenthesis.

Example
For s = "((", the output should be
flipForBalance(s) = 1.
"""

# solution by ernie_y
# def flipForBalance(s):
#    a = []
#    n = 0
#    for i in s:
#        if i == ")":
#            if a:
#                if a[-1] == "(":
#                    a.pop()
#                else:
#                    a += i,
#            else:
#                n += 1
#                a += "("
#        else:
#            a += i,
#    return n+len(a)/2

t = r = 0
for i in eval(dir()[0])[0]:
    t += .5
    t -= "(" < i
    r += t < 0
    t += t < 0
return r + t
