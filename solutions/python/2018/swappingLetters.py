"""
Albert is playing with text. Instead of writing sentences as they should be, he decided to randomly swap pairs of letters in them. But not even in the whole text, only from some place in the middle of the text onward. At least he marked the places in the text, where each substitution starts, and what two letters are swapped. But the text is still hard to read. Could you please decode it back to its original form?

Beginning of each substitution is marked by the sequence "[A<->B]" in the input text. It means that the letters A and B are swapped from now on. The sequence itself should be removed from the text.

Caveat - swaps are transitive but not commutative. Given two swaps [A<->B] and [B<->C], the string "ABC" should be decoded as "BCA". Given the same swaps in opposite order, [B<->C], [A<->B], the string "ABC" should be decoded as "CAB".

Example
For text = "Once upon a[e<->r] timr threr [a<->l]wls l alnd whrer King Labret euard.", the output should be
swappingLetters(text) = "Once upon a time there was a land where King Albert ruled.".
The first three words remain the same because the first swap mark comes only after the third word. From then on, every letter 'E' is replaced by 'R' and vice versa. After two more words, there is another swap - this time, 'A' is replaced by 'L' and vice versa. But keep in mind that 'E' and 'R' are still being swapped, too.
"""


def swappingLetters(t):
    # by rgtichy
    p = len(t) - 1
    o = ""
    while p >= 0:
        if t[p] == ']' and t[p - 3] == '-':
            B = t[p - 1]
            B += B.upper()
            A = t[p - 5]
            A += A.upper()
            o = o.translate(o.maketrans(A + B, B + A))
            p -= 7
        else:
            o += t[p]
            p -= 1
    return o[::-1]
