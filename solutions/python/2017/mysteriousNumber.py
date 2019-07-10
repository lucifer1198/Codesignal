"""
This is a reverse challenge, enjoy!

A reverse challenge is a special type of challenge, where no description is provided!
You have to solve two challenges in one: find out what the author wants from you and write a solution. Check out this page for more information.

this page: https://codefights.com/forum/oJpnZsJF5udPgq3Kd

Input/Output

[time limit] 4000ms (py3)

[input] integer n

Guaranteed constraints:
1 ≤ n ≤ 26.

[output] char
"""

# solution by sifulan

# 1 = "Q"
# 2 = "W"
# 3 = "E"
# 4 = "R"
# 7 = "U"
# this about keyboard `QWERTY`


# 93 chars
# def mysteriousNumber(n):
#    d = {}
#    for k, v in enumerate('QWERTYUIOPASDFGHJKLZXCVBNM'):
#        d[k+1] = v
#    return d[n]


# 87 chars
n, = eval(dir()[0])
d = {}
for k, v in enumerate('QWERTYUIOPASDFGHJKLZXCVBNM'):
    d[k + 1] = v
return d[n]

# 65 chars
n, = eval(dir()[0])
q = list('QWERTYUIOPASDFGHJKLZXCVBNM')
return q[n - 1]

# 62 chars
n, = eval(dir()[0])
return list('QWERTYUIOPASDFGHJKLZXCVBNM')[n - 1]

# 56 chars
n, = eval(dir()[0])
return 'QWERTYUIOPASDFGHJKLZXCVBNM'[n - 1]
