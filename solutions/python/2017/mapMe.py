"""
This is a reverse challenge, enjoy!
"""


def mapMe(s):
    # by ben_w6
    r = '['
    for x in range(32):
        t = ','.join(c for c in s if ord(c) % 32 == x)
        if t:
            r += `x` + ':[%s],' % t
    return r[:-1] + ']'

# by ernie_y
# def mapMe(s):
#    D = {}
#    for i in s:
#        o = ord(i)%32
#        D[o] = D.get(o,[])+[i]
#    J = ','.join
#    return '[%s]'%J( `i`+':[%s]'%J(D[i]) for i in sorted(D))

# by ernie_y
J = ','.join
u = '[%s]'
mapMe = lambda s: u % J('%d:' % i + u % j for i in range(32)
                        for j in [J(j for j in s if ord(j) % 32 == i)] if j)
