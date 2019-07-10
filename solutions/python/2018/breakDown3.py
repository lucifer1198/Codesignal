"""
Last one was a bit easy. Let's ramp it up a tad :)

This challenge is close to the real deal. Some of you may get it here. Solve the equation for X.

Example
For string = "99X=1(mod 8)", the output should be
breakDown3(string) = 3.
"99X=1(mod 8)".

To solve this equation, first you must reduce the left side. Make it as small as possible without being negative by decreasing it by mod. So, for example
99X
would reduce to
3x.
Now your expression should look like this:
3X=1(mod 8).
Now that the left side is done, we switch focus to the right side. If we mod by 8, we can safely add or subtract 8 to get the same answer, so we add 8 to the number on the right until we get a number evenly divisible by the left number. So
3X=1(mod 8)
goes to
3x=9(mod 8).
9 is evenly divided by 3, so we stop there. Our final step is to isolate X, so we divide 9 by 3 leaving us with
X=3.
"""


def breakDown3(s):
    l, r, m = map(int, re.findall("\d+", s))
    while r % l:
        r += m
    return r / l
