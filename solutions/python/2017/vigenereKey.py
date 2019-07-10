"""
Hello! It's me again. Thanks for the help last time, although once again it became kind of a disaster...
Ahaha. I think I went too far again in my "creative" poem writing.

Anyway, this time it's a different problem. Here are some text that I found in one of my old notebooks.
They come in pairs, one of each is a normal English sentence (and actually, I recognize some of them are my poem),
and another looks like some seemly random letters. I complete forgot when, where or why I wrote it down,
but somehow I remember these text are related by something called Vigenère cipher.
I think the "random" text is the encoded version of the original sentence,
but figuring out the key is a little bit tedious to do by hand.
So I want to ask you to write a program to figure out the shortest possible key for each pair of text.
For both your convenience and not let the disaster happen again, I removed all non-letters in these texts,
and converts all letters to lowercase. Besides, the cipher only works on letters anyway, so... yeah.

Example

For original = "okayeveryone", cipher = "qvuzggysazhf",
the answer would be vigenereKey(original, cipher) = "club".

The corresponding encoding process would be:

original: okayeveryone
key:      clubclubclub
cipher:   qvuzggysazhf

The key that will produce this process can be either "club", "clubclub", or "clubclubclub", but "club" is the shortest one.
"""

# solution by hydralisk

k = w = ''
for a, b in zip(*eval(dir()[0])):
    k += chr(97 + (ord(b) - ord(a)) % 26)

for c in k:
    w += c
    if k in w * 1000:
        return w
