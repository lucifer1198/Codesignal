# solution by erine_y, py3

bijectiveNumeration = lambda n, d: d[n//100]+"%03d"%~(~-n%99)

"""
You need to label a set of indices; ideally something a little more human friendly than just a number.

What was decided was to use a character, or set of characters, hyphenated with a two digit number.

Example
For n = 134 and domain = ["MONKEYS", "PENGUINS", "ZEBRAS", "LIONS"], the output should be
bijectiveNumeration(n, domain) = "PENGUINS-35".
An output of MONKEYS-01 for n=1, MONKEYS-99 for n=99, PENGUINS-01 for n=100 and so on.
"""
