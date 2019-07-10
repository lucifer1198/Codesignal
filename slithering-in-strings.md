### 1. String Definition

Which of the given string definitions are incorrect?

```
s = 'abacaba'
s = "abacaba"
s = ''abacaba''
s = ""abacaba""
s = '''abacaba'''
s = """abacaba"""
```

a. Definitions 3 and 4. [check]

### 2. Fix Message

One of your friends has an awful writing style: he almost never starts a message with a capital letter, but adds uppercase letters in random places throughout the message. It makes chatting with him very difficult for you, so you decided to write a plugin that will change each message received from your friend into a more readable form.

Implement a function that will change the very first symbol of the given message to uppercase, and make all the other letters lowercase.

Example

```
For message = "you'll NEVER believe what that 'FrIeNd' of mine did!!1",
the output should be
fixMessage(message) = "You'll never believe what that 'friend' of mine did!!1".
```

**Answer:**

```python
def fixMessage(message):
    return message.capitalize() # this line
```

### 3. Cat Walk

You've been working on a particularly difficult algorithm all day, and finally decided to take a break and drink some coffee. To your horror, when you returned you found out that your cat decided to take a walk on the keyboard in your absence, and pressed a key or two. Your computer doesn't react to letters being pressed when an unauthorized action appears, but allows typing whitespace characters and moving the arrow keys, so now your masterpiece contains way too many whitespace characters.

To repair the damage, you need to start with implementing a function that will replace all multiple space characters in the given line of your code with single ones. In addition, all leading and trailing whitespaces should be removed.

Example

```
For line = "def      m   e  gaDifficu     ltFun        ction(x):",
the output should be
catWalk(line) = "def m e gaDifficu ltFun ction(x):".
```

**Answer:**

```python
def catWalk(code):
    return ' '.join(code.split()) # this line
```

### 4. Convert Tabs

You found an awesome customizable Python IDE that has almost everything you'd like to see in your working environment. However, after a couple days of coding you discover that there is one important feature that this IDE lacks: it cannot convert tabs to spaces. Luckily, the IDE is easily customizable, so you decide to write a plugin that would convert all tabs in the code into the given number of whitespace characters.

Implement a function that, given a piece of code and a positive integer x will turn each tabulation character in code into x whitespace characters.

Example

```
For code = "\treturn False" and x = 4, the output should be
convertTabs(code, x) = "    return False".
```

**Answer:**

```python
def convertTabs(code, x):
    return code.replace('\t', ' '*x)
```

### 5. Feedback Review

You've launched a revolutionary service not long ago, and were busy improving it for the last couple of months. When you finally decided that the service is perfect, you remembered that you created a feedbacks page long time ago, which you never checked out since then. Now that you have nothing left to do, you would like to have a look at what the community thinks of your service.

Unfortunately it looks like the feedbacks page is far from perfect: each feedback is displayed as a one-line string, and if it's too long there's no way to see what it is about. Naturally, this horrible bug should be fixed. Implement a function that, given a feedback and the size of the screen, splits the feedback into lines so that:

- each token (i.e. sequence of non-whitespace characters) belongs to one of the lines entirely;
- each line is at most size characters long;
- no line has trailing or leading spaces;
- each line should have the maximum possible length, assuming that all lines before it were also the longest possible.

**Example**

For feedback = "This is an example feedback", and size = 8,
the output should be

```
feedbackReview(feedback, size) = ["This is", 
                                  "an", 
                                  "example", 
                                  "feedback"]
```

**Answer:**

```python
import textwrap

def feedbackReview(feedback, size):
    return textwrap.wrap(feedback, size)
```

### 6. Is Word Palindrome

Given a word, check whether it is a palindrome or not. A string is considered to be a palindrome if it reads the same in both directions.

Example

```
For word = "aibohphobia", the output should be
isWordPalindrome(word) = true;

For word = "hehehehehe", the output should be
isWordPalindrome(word) = false.
```

**Answer:**

```python
def isWordPalindrome(word):
    return word == word[::-1]
```

### 7. Permutation Chiper

You found your very first laptop in the attic, and decided to give in to nostalgia and turn it on. The laptop turned out to be password protected, but you know how to crack it: you have always used the same password, but encrypt it using permutation ciphers with various keys. The key to the cipher used to protect your old laptop very conveniently happened to be written on the laptop lid.

Here's how permutation cipher works: the key to it consists of all the letters of the alphabet written up in some order. All occurrences of letter 'a' in the encrypted text are substituted with the first letter of the key, all occurrences of letter 'b' are replaced with the second letter from the key, and so on, up to letter 'z' replaced with the last symbol of the key.

Given the password you always use, your task is to encrypt it using the permutation cipher with the given key.

Example

```
For password = "iamthebest" and
key = "zabcdefghijklmnopqrstuvwxy", the output should be
permutationCipher(password, key) = "hzlsgdadrs".
```

Here's a table that can be used to encrypt the text:

```
abcdefghijklmnopqrstuvwxyz
||  |  ||   |     || 
vv  v  vv   v     vv
zabcdefghijklmnopqrstuvwxy
```

**Answer:**

```python
def permutationCipher(password, key):
    table = {ord(i): key[(ord(i))-97] for i in password }
    return password.translate(table)
```
