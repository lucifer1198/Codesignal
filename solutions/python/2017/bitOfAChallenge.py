"""
This is a reverse challenge, enjoy!

A reverse challenge is a special type of challenge, where no description is provided!
You have to solve two challenges in one: find out what the author wants from you and write a solution.
Check out [this page] for more information.

[this page] https://codefights.com/forum/oJpnZsJF5udPgq3Kd

"""

# solutions by sifulan

# 100 chars
# def bitOfAChallenge(n):
#    one = int(bin(n).replace('0b', '').count('1'))
#    return string.ascii_uppercase[one-1]

# 91 chars
# n, = eval(dir()[0])
# o = int(bin(n).replace('0b', '').count('1'))
# return string.ascii_uppercase[o - 1]

# 85 chars
# n, = eval(dir()[0])
# o = int(bin(n).replace('0b', '').count('1'))
# return string.ascii_uppercase[o - 1]

# 79 chars
# n, = eval(dir()[0])
# o = int(bin(n)[1::].count('1'))
# return string.ascii_uppercase[o - 1]

# 78 chars
# o = int(bin(eval(dir()[0])[0])[1::].count('1'))
# return string.ascii_uppercase[o - 1]

# 75 chars
# return string.ascii_uppercase[int(bin(eval(dir()[0])[0])[1::].count('1')) - 1]

# 70 chars
return string.ascii_uppercase[bin(eval(dir()[0])[0])[1::].count('1') - 1]

# 66 chars, with python2
bitOfAChallenge = lambda n: string.uppercase[bin(n)[1::].count('1') - 1]

# 64 chars, with python2
return string.uppercase[bin(eval(dir()[0])[0])[1::].count('1') - 1]
