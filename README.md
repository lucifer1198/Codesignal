# Codesignal
Arcade Competition &amp; Codefights

### 1. What will be the value of res after the following snippet is executed:

```python
xs = [()]
res = [False] * 2

if xs:
    res[0] = True
if xs[0]:
    res[1] = True

print(res) # [True, False]
```

### 2. Efficient comparison

You would like to write a function that takes integer numbers x, y, L and R as parameters 
and returns True if xy lies in the interval (L, R] and False otherwise. 
You're considering several ways to write a conditional statement inside this function:

```
if L < x ** y <= R:
if x ** y > L and x ** y <= R:
if x ** y in range(L + 1, R + 1):
```

What option would be the most efficient in terms of execution time?

> Let test it out at https://www.tutorialspoint.com/execute_python_online.php

```python
x = True
y = True
L = True
R = True

def test1():
    if L < x ** y <= R:
        return True
    return False

def test2():
    if x ** y > L and x ** y <= R:
        return True
    return False

def test3():
    if x ** y in range(L + 1, R + 1):
        return True
    return False


# test performance

import timeit

t1 = timeit.Timer(setup='from __main__ import test1', stmt='test1()')
t2 = timeit.Timer(setup='from __main__ import test2', stmt='test2()')
t3 = timeit.Timer(setup='from __main__ import test3', stmt='test3()')

print(t1.timeit()) # 3.44227409363
print(t2.timeit()) # 3.26994419098
print(t3.timeit()) # 7.79589700699
```

> I just think why `c. Option 1 is the most optimal one?` and why not `Option 2 is the most optimal one?`

- a. Options 1 and 2 are equally good (and better than option 3).
- b. Option 2 is the most optimal one.
- c. Option 1 is the most optimal one. [check]
- d. All approaches are fine.
- e. Option 3 is the most optimal one.


### 3. Special Condition

One of the given statements doesn't work the same way others do. Which one?
Assume that a and b are boolean variables.

- a. not (a == b)
- b. a == (not b) [check]
- c. a == not b
- d. not a == b

### 4. Language Differences

Your friend, an experienced coder, has just started to learn Python. Since he is already proficient in Java and C++, he decided to write all his snippets in all three languages to test his Python code. Here's the very first function your friend wrote in Python and Java (the C++ version is the same as Java one):

```python
def division(x, y):
    return x // y
```

```java
in division(int x, int y) {
    return x / y;
}
```

You noticed that the functions aren't quite the same: they won't produce the same result for some valid values of x and y. Which ones?

- a. x = 15, y = -4 [check]
- b. x = -8, y = 2
- c. x = -8, y = 2
- d. x = 17, y = 13
- e. x = 5, y = 10

### 5. Count Bits

Implement a function that, given an integer n, uses a specific method on it and returns the number of bits in its binary representation.

Note: in this task and most of the following tasks you will be given a code snippet with some part of it replaced by the ellipsis (...). Only this part is allowed to be changed.

Example

```
For n = 50, the output should be
countBits(n) = 6.
```

5010 = 1100102, a number that consists of 6 digits. Thus, the output should be 6.

* Input/Output
    - [time limit] 4000ms (py3)
    - [input] integer n

* A positive integer.

* Guaranteed constraints:
    - 1 ≤ n ≤ 109.

* [output] integer
    - The number of bits in binary representation of n.


**Answer:**

```python
def countBits(n):
    return n.bit_length()
```

### 6. Modulus

It frustrates you more than you'd like to admit that the modulus operator in Python can be applied to non-integer values. When you write code, you expect the result of the modulus operator to always be an integer, but thanks to Python this isn't always the case.

To fix this, you've decided to write your own modulus operator as a function. Your task is to implement a function that, given a number n, returns -1 if this number is not an integer and n % 2 otherwise. It is guaranteed that if the number represents an integer, it will be written without a decimal point.

Example

```
For n = 15, the output should be
modulus(n) = 1;

For n = 23.12, the output should be
modulus(n) = -1.
```

- Input/Output
    - [time limit] 4000ms (py3)
    - [input] numeric n

- A non-negative number that can be an int, a float, or a long.

- Guaranteed constraints:
    - 0 ≤ n ≤ 1000

- [output] integer
    - Return n % 2 if n is an integer, otherwise return -1.

**Answer:**

```python
def modulus(n):
    if isinstance(n, int):
        return n % 2
    else:
        return -1
```

### 7. Simple Short

To understand how efficient the built-in Python sorting function is, you decided to implement your own simple sorting algorithm and compare its speed to the speed of the Python sorting. Write a function that, given an array of integers arr, sorts its elements in ascending order.

Hint: with Python it's possible to swap several elements in a single line. To solve the task, use this knowledge to fill in both of the blanks (...).

Example

```
For arr = [2, 4, 1, 5], the output should be
simpleSort(arr) = [1, 2, 4, 5].
```

- Input/Output
    - [time limit] 4000ms (py3)
    - [input] array.integer arr

- Guaranteed constraints:
    - 1 ≤ arr.length ≤ 100,
    - -105 ≤ arr[i] ≤ 105.

- [output] array.integer
    - The given array with elements sorted in ascending order.


**Answer:**

```python
def simpleSort(arr):

    n = len(arr)

    for i in range(n):
        j = 0
        stop = n - i
        while j < stop - 1:
            if arr[j] > arr[j + 1]:
                arr[j],arr[j+1] = arr[j+1],arr[j] # answer is this line
            j += 1
    return arr
```

### 8. Base Conversion

Your university professor decided to have a little fun and asked the class to implement a function that, given a number n and a base x, converts the number from base x to base 16. To make things more interesting, he announced that the first student to write the solution will have to answer fewer question than the rest of the class during the final exam.

Laughing devilishly, you asked if it was okay to use a language of your choice, and the unsuspecting professor answered "yes". It's settled then: Python is your language of choice!

Now you're bound to win. Implement a function that, given an integer number n and a base x, converts n from base x to base 16.

Example

```
For n = "1302" and x = 5, the output should be
baseConvertion(n, x) = "ca".

Here's why:
13025 = 20210 = ca16.
```

- Input/Output
    - [time limit] 4000ms (py3)
    - [input] string n

- A valid non-negative integer in base x. The string is guaranteed to consist of digits and lowercase English letters.

- Guaranteed constraints:
    - 1 < n.length ≤ 10.

- [input] integer x
    - The base of n.

- Guaranteed constraints:
    - 2 ≤ x ≤ 36.

- [output] string

The value of n in base 16. The string should contain only digits and lowercase English letters 'a' - 'f'.

**Answer**

```python
def baseConversion(n, x):
    return hex(int(n, x))[2:] # answer is this line
```


### 9. Mex Function

You've just started to study impartial games, and came across an interesting theory. The theory is quite complicated, but it can be narrowed down to the following statements: solutions to all such games can be found with the mex function. Mex is an abbreviation of minimum excludant: for the given set s it finds the minimum non-negative integer that is not present in s.

You don't yet know how to implement such a function efficiently, so would like to create a simplified version. For the given set s and given an upperBound, implement a function that will find its mex if it's smaller than upperBound or return upperBound instead.

Hint: for loops also have an else clause which executes when the loop completes normally, i.e. without encountering any breaks

Example

```
For s = [0, 4, 2, 3, 1, 7] and upperBound = 10,
the output should be
mexFunction(s, upperBound) = 5.

5 is the smallest non-negative integer that is not present in s, and it is smaller than upperBound.

For s = [0, 4, 2, 3, 1, 7] and upperBound = 3,
the output should be
mexFunction(s, upperBound) = 3.

The minimum excludant for the given set is 5, but it's greater than upperBound, so the output should be 3.
```

- Input/Output
    - [time limit] 4000ms (py3)
    - [input] array.integer s

- Array of distinct non-negative integers.

- Guaranteed constraints:
    - 0 ≤ s.length ≤ 100,
    - 0 ≤ s[i] ≤ 100.

- [input] integer upperBound

- A positive integer.

- Guaranteed constraints:
    - 1 ≤ upperBound ≤ 100.

- [output] integer

Mex of s if it's smaller than upperBound, or upperBound instead.

**Answer**

```python
def mexFunction(s, upperBound):
    found = -1
    for i in range(upperBound):
        if not i in s:
            found = i
            break
    else:
        found = upperBound # this line

    return found
```

### 10. List Beautifier

Let's call a list beautiful if its first element is equal to its last element, or if a list is empty. Given a list a, your task is to chop off its first and its last element until it becomes beautiful. Implement a function that will make the given a beautiful as described, and return the resulting list as an answer.

Hint: one of the features introduced in Python 3 called extended unpacking could help here.

Example

```
For a = [3, 4, 2, 4, 38, 4, 5, 3, 2], the output should be
listBeautifier(a) = [4, 38, 4].

Here's how the answer is obtained:
[3, 4, 2, 4, 38, 4, 5, 3, 2] => [4, 2, 4, 38, 4, 5, 3] => [2, 4, 38, 4, 5] => [4, 38, 4].

For a = [1, 4, -5], the output should be
listBeautifier(a) = [4].
```

- Input/Output
    - [time limit] 4000ms (py3)
    - [input] array.integer a

- A list of integers.

- Guaranteed constraints:
    - 0 ≤ a.length ≤ 50,
    - 1 ≤ a[i] ≤ 100.

- [output] array.integer

A beautiful list obtained as described above.

**Answer**

```python
def listBeautifier(a):
    res = a[:]
    while res and res[0] != res[-1]:
        a, *res, b = res # this line
    return res
```

