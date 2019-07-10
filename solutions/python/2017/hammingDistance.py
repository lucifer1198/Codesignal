def hammingDistance(string1, string2):
    if len(string1) != len(string2):
        return None
    return sum(el1 != el2 for el1, el2 in zip(string1, string2))

"""
Given two strings, calculate the Hamming distance between them.

Example

For string1 = "abab" and string2 = "cbad", the output should be
hammingDistance(string1, string2) = 2.

Only the first and the last characters are different.

Input/Output

[time limit] 4000ms (py3)
[input] string string1

The first string.

Guaranteed constraints:
3 ≤ string1.length ≤ 10.

[input] string string2

The second string.

Guaranteed constraints:
3 ≤ string2.length ≤ 10.

[output] integer

Hamming distance between string1 and string2.
"""
