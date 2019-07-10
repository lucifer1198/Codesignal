"""
Given a string that presents an arithmetic predicate that may consist
"*, +, -, /, (, )" and digits (0 to 9).
The predicate has only one equals sign "=".

Note 1: operator precedence is important!

Note 2: all numbers in the predicate are initially less than 10 and non-negative!

Write a function that takes that string and tells if it is correct or not!

Example

For predicate = "( 3 * ( 7 - 1 ) - 6 ) / 3 = 4" , the output should be
arithmeticPredicate(predicate) = true.

For predicate = "1 + 4 = 2 * 3", the output should be
arithmeticPredicate(predicate) = false.
"""

# solution by sifulan

# 140 chars
# def arithmeticPredicate(predicate):
#    splited = predicate.split('=')
#    left    = splited[0]
#    right   = splited[1]
#
#    if eval(left) == eval(right):
#        return True
#    return False

# 77 chars
# p, = eval(dir()[0])
# s  = p.split('=')
#
# if eval(s[0]) == eval(s[1]):
#    return True
# return False

# 71 chars
# e  = eval
# p, = e(dir()[0])
# s  = p.split('=')
#
# return True if e(p[0]) == e(p[1]) else False

# 70 chars
e = eval
p = e(dir()[0])[0].split('=')

return True if e(p[0]) == e(p[1]) else False
