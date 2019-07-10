"""
I define a shortened string as a string after being shortened from a full-string (a full-string is a string just contains uppercase English letters) and it follows the rules:

Xm - The character X rewrites m times;
(S)m - The string S rewrites m times.
For example, "H3A" is a shortened string of "HHHA".
(HDL)5 is a shortened string of "HDLHDLHDLHDLHDL".
(AH0)2AD is a shortened string of "AAAD".

Given a shortened string, return its full-string.

Example
For ss = "KB2 (Y2F)2 B5A". the output should be
shortenedString(ss) = "KBBYYFYYFBBBBBA".
"""

# solution by hydralisk

# r = re.sub
# def shortenedString(s):
#    s = r("(\d+)", r"*\1", s)
#    s = r("([A-Z])", r"'\1'", s)
#    s = r("(\(*\'\w)", r"+\1", s)
#    return eval(s[1:])

# r = re.sub
# return eval(r("(\(*'\w)", r"+\1", r("([A-Z])", r"'\1'", r("(\d+)", r"*\1", *eval(dir()[0])))))

# r = re.sub
# def shortenedString(s):
#    s = r("([A-Z])", r"  '\1'", s)
#    s = r("(\(*  ')", r"+\1", s)
#    s = r("(\d+)", r"*\1", s)
#    return eval(s[1:])

r = re.sub
return eval(r("(\d+)", r"*\1", r("(\(*  ')", r"+\1", r("([A-Z])", r"  '\1'", *eval(dir()[0]))))[1:])
