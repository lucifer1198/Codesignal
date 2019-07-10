"""
One of your friends noticed that you could enumerate the alphabet and sum the letters of your name to get a number.
For example, if your name is Diego, your number would be 4 + 9 + 5 + 7 + 15 = 40.

She also notices that most names have different numbers, but there are some names that have the same sum, like Bob and Dan.
Your friend is convinced that if two people have the same same sum, they are destined to be best friends.

Now, your friend doesn't like adding too much, and has asked you to write a function that takes two names and tells if they are destined to be best friends or not.

Note that names can contain spaces, that should be ignored.

Example
For name1 = "Bob" and name2 = "Dan", the output should be

bestFriendNames(name1, name2) = true.
"""

# solutions by sifulan

# 175 chars
# def bestFriendNames(name1, name2):
#    ascii = string.ascii_lowercase
#    total = lambda n: sum(ascii.index(c)+1 for c in n.lower().replace(' ', ''))
#    if total(name1) == total(name2):
#        return True
#    return False

# 129 chars
# x, y = eval(dir()[0])
# t = lambda n: sum(string.ascii_lowercase.find(c)+1 for c in n.lower().replace(' ', ''))
# if t(x) == t(y):
#    return True
# return False

# 126 chars
x, y = eval(dir()[0])
t = lambda n: sum(string.ascii_lowercase.find(c) + 1 for c in n.lower().replace(' ', ''))
return True if t(x) == t(y) else False

# this python2, using: `string.lowercase`
# 120 chars
x, y = eval(dir()[0])
t = lambda n: sum(string.lowercase.find(c) + 1 for c in n.lower().replace(' ', ''))
return True if t(x) == t(y) else False
