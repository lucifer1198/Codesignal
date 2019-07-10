"""
Given a single character, an English vowel; find the next vowel.
Vowels are listed from alphabetical order: 'A', 'E', 'I', 'O', 'U'.

Example
For vowel = 'A', the output should be
nextVowel(vowel) = 'E'.
"""

# def nextVowel(v):
#    vs = ['A', 'E', 'I', 'O', 'U']
#    return vs[vs.index(v)+1]

# i = eval(dir()[0])[0]
# v = 'A E I O U'.split()
# return v[v.index(i)+1]

# i = eval(dir()[0])[0]
# v = 'AEIOU'
# return v[v.index(i)+1]

# 66 chars
def nextVowel(i):
    v = 'AEIOU'
    try:
        return v[v.index(i)+1]
    except:
        return 'A'

# 57 chars
v = 'AEIOU'
nextVowel = lambda i: 'A' if i == 'U' else v[v.index(i)+1]
