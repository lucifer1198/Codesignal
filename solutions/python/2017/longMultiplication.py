def longMultiplication(A, B):
    c = a = i = 0
    R = [0]*9999
    for x in B[::-1]:
        
        j = i
        for y in A[::-1]+'0':
            a += c > 0
            c += int(x)*int(y)
            R[j] += c%10
            c //= 10
            
            j += 1
        i += 1
            
    for X in R:
        a += c > 0
        c += X
        c //= 10
    
    return a

"""
Recently there have been several challenges which require the manipulation of very large numbers. If your favorite language has built-in support for big integers you might not have given this second thought, therefor in the interest of spreading the joy you will now need to implement multiplication of two integers the good-old fashioned way.

Now, before you start hatching up a plan to cheat using built-in big integers, for this challenge you need to return the number of carry operations.

Reminder, calculating a · b

a=123
b=45

First find 123 · 5

11
---
123
  5
---
615
This yields two carry operations

Next find 123 · 4, padding one zero to the right:

  1
----
 123
   4
----
4920
This yields one additional carry

Now sum 615 + 4920

1
----
 615
4920
----
5535
This again yields one carry operation

The total number of carry operations therefore is 4.

Counting carry operations

Although the product does not depend on the order of a and b, for counting carry operations it is important that you perform a · b and not b · a;
Only count carry operations, the actual amount carried is not important;
First find all the sub multiplication results, then sum them all at once. During the summation each column can generate 0 or 1 carry operations, for instance a column containing [9, 8, 7] only counts as a single carry operation even though any two of these numbers would generate a carry operation.
Example
For a = "123" and b = "45", the output should be
longMultiplication(a, b) = 4.

Input/Output

[time limit] 4000ms (py3)
[input] string a

The first number.

Guaranteed constraints:
1 ≤ a.length < 850.

[input] string b

The second number.

Guaranteed constraints:
1 ≤ a.length < 850.

[output] integer

The number of carry operations performed while multiplying a by b.
"""
