"""
Given a list of strings g and an integer z, sort the strings by the zth 1-based character ignoring the characters' case.

In case of a tie, the first element that appears in g should go first.

Example

For g = ["Cow", "Chicken", "Deer", "Rabbit"] and z = 3,
the output should be

sortByZ(g, z) = ["Rabbit", "Deer", "Chicken", "Cow"].

* The hidden test (you should pass it):

thank for: आदर्श_भ
    g: ["ApPLe", "PupmpKIn", "Ba1ana", "PaSTa", "Pizza", "Two2"]
    z: 3

Output should be:
    ["Ba1ana", "Two2", "ApPLe", "PupmpKIn", "PaSTa", "Pizza"]
"""

# solution by sifulan
#
# 58 chars
# def SortByZ(g, z):
#    return sorted(g, key=lambda x: x[z - 1].lower())

# 57 chars
# def SortByZ(g, z):
#    g.sort(key=lambda x: x[z - 1].lower())
#    return g

# 54 chars
SortByZ = lambda g, z: sorted(g, key=lambda x: x[z - 1].lower())
