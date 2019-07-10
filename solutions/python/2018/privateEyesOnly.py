"""
The captain has just intercepted a message from the opposition.
But they were clever (or not?) enough to encode it using the Caesar Cipher,
leaving the captain unable to get the information he needed.

Having zero patience with figuring out the right number themselves,
they ask for you and the IT department's help to crack the message.

You and the IT department are bored as well, and decide to just mess around
and see who can make a program that can crack the encoded string (Nobody wants to shift it 26 times, that's boring and tedious!)

Example
For messge = "Uijt jt b sfbebcmf tusjoh jo Fohmjti!", the output should be
privateEyesOnly(message) = "This is a readable string in English!".

Out of all the 26 possible shifts, the only readable (and valid) string is when you shift 25 times "This is a readable string in English!".
"""


def privateEyesOnly(message):
    # solution by yoku_benkyo
    v = 'etaoinshrdlcumwfgypbvkjxqz'
    z = 'abcdefghijklmnopqrstuvwxyz'
    s = 0
    key = -1
    for i in range(26):
        c = [0] * 26
        for j in message:
            try:
                c[v.index(z[(z.index(j.lower()) - i) % 26])] += 1
            except ValueError:
                pass
        score = 0
        for j, k in enumerate(c):
            score += k * (26 - j)
        if s < score:
            key = i
            s = score
    t = ''
    for i in message:
        try:
            k = (z.index(i.lower()) - key) % 26
            if i.isupper():
                t += z[k].upper()
            else:
                t += z[k]
        except ValueError:
            t += i
    return t
