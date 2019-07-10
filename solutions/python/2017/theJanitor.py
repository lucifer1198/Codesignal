"""
In one city it is allowed to write words on the buildings walls.
The local janitor, however, doesn't approve of it at all. Every night he vandalizes the writings by erasing all occurrences of some letter.
Since the janitor is quite lazy, he wants to do this with just one swipe of his mop.

Given a word, find the minimum width of the mop required to erase each of the letters.

Example

For word = "abacaba", the output should be
theJanitor(word) = [7, 5, 1, 0, 0, ..., 0, 0] (26 elements altogether).

Input/Output

[time limit] 4000ms (py3)

[input] string word

A word consisting of only lowercase Latin letters.

Guaranteed constraints:

5 ≤ word.length ≤ 50.

[output] array.integer

An array of length 26. The first element is the minimum width of the mop to erase letter 'a', the second - letter 'b' etc.
"""

w, = eval(dir()[0])
z = [0] * 26

for c in set(w):
    z[ord(c) - 97] = len(w) - w.index(c) - w[::-1].index(c)

return z
