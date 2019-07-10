"""

Given an integer n, find the nth number in Pascal's Triangle (https://en.wikipedia.org/wiki/Pascal%27s_triangle).

Example

For n = 5, the output should be
nthPascalNumber(n) = 2.

The first few lines of the triangle are:

1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
1 5 10 10 5 1

The 5th element is 2.

"""

# solution by sifulan

# 200 chars
# def nthPascalNumber(n):
#    lst = [1]
#    out = []
#
#    for i in range(n):
#        out.extend(lst)
#        newlist = []
#        newlist.append(lst[0])
#
#        for i in range(len(lst)-1):
#            newlist.append(lst[i]+lst[i+1])
#
#        newlist.append(lst[-1])
#        lst = newlist
#
#    return out[n-1]


# 143 chars
# n, = eval(dir()[0])
# l = [1]
# o = []
#
# for i in range(n):
#    o.extend(l)
#
#    d = []
#    d.append(l[0])
#
#    for x in range(len(l)-1):
#        d.append(l[x] + l[x+1])
#
#    d.append(l[-1])
#    l = d
#
# return o[n-1]


# 96 chars
n, = eval(dir()[0])
t = [1]
y = [0]
o = []

for x in range(n):
    o.extend(t)
    t = [l + r for l, r in zip(t + y, y + t)]
return o[n - 1]
