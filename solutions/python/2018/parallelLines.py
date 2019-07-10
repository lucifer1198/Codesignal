"""
Two lines ax + by + c = 0 and a'x + b'y + c' = 0 are parallel if and only if
a * b' = b * a'.

Check if the two given lines are parallel.

Example

For line1 = [1, -1, 0] and line2 = [1, 1, 0], the output should be
parallelLines(line1, line2) = false.
"""


def parallelLines(line1, line2):
    return line1[0] * line2[1] == line1[1] * line2[0]
