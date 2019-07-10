"""
This is a reverse challenge challenge, enjoy!
"""

s = 0
for i in eval(dir()[0])[0].encode():
    if i >> 7:
        i = 256 - i
    s += 2**i % i == 2
return s
