"""
You will be given a 2D matrix of English lower case letters.
Your mission today is to find the longest path that following these rules below.

The path can only be straight line or form a 90 degree corner;
In each step, the next letter must be different from the current letter;
The path cannot cut itself or form a loop path;
If there are more than one longest path, pick the highest one.
Example
For

letterMap =
a   b   c
d   e   f
g   h   i
the output should be
letterPath(letterMap) = "ihgdefcba".

In this example, we have several longest paths: abcfihgde, adghifcbe, edghifcba, etc.
The highest one is the final answer ihgdefcba
"""

# solution by ant0n


def letterPath(m):
    b = (0, '')
    h = len(m) + 1

    def u(o, t=0, s=''):
        nonlocal b
        try:
            e = m[o % h][o // h]
            c = 2**o
            t += c
            if c & t and e != s[-1:]:
                s += e
                b = max((len(s), s), b)
                for d in (-1, 1, -h, h):
                    u(o + d, t, s)
        except:
            o
    if h > 1:
        for i in range(h * len(m[0])):
            u(i)
    return b[1]
