"""
Your teacher recently gave you some math equations to solve.
The only thing is that not all of the equations are valid.
You don't want to find this out the hard way, so you create a function to determine if an equation is valid or not.
Parts of an Equation:

Numbers
Numbers will range from -104 to 104.
Operators
Operators include:
Addition: " + "
Subtraction: " - "
Multiplication: " * "
Division: " / "
Exponents: " ^ "
Parentheses
Parentheses look like " ( " and " ) ".
Variables
Variables are lowercase, single letters from "a" to "z".
Equals Sign
An equals sign will be used to separate the two halves of the equation. It looks like " = ".

Rules:

Equations must consist of two sides separated by an equal sign.
Equations cannot have any operators or variables back-to-back.
Note that equations can contain powers. Instead of using " ** ", use " ^ ".
Equations must only contain numbers, operators, parentheses, and variables.
An exception is the equals sign " = ".
Parenthesis must be in a logical order.

Note that for this challenge, a multiplication symbol must separate all back-to-back parenthesis. Instead of ")(", use ") * (".
Also, act as if all equations follow the same rules they do in real life.
Don't let operators dangle at the beginnings or endings of each side, don't have multiple equal signs, etc.
If you have any questions, ask me in the comments section.
For the purposes of this challenge, assume whitespaces don't matter.
This shouldn't affect anything, though. I will try to keep the equation spaced appropriately to help.
Finally, an equation does not have to have a single solution for it to be valid.
An equation can also have no solutions, infinite solutions, or multiple solutions.

Note: For the purpose of this challenge, assume that no two operators can be back-to-back.
This includes subtracting, adding, multiplying, and dividing negative numbers, along with putting a number to the power of a negative.

Example

For equation = "5 + 5 = 10", the output should be
validEquation(equation) = true;

For equation = "5", the output should be
validEquation(equation) = false;

For equation = "5 & 2 = 3", the output should be
validEquation(equation) = false.
"""

# solution by ernie_y
# r = c = 0
# e = ''
# for i in eval(dir()[0])[0]:
#    if i < "*":
#        c += ' ('.find(i)
#    else:
#        e += i
#    if i == "=":
#        r += 1
#        if c!=0:
#            break
# return c<1==r and not re.findall('[a-z]{2}|^\W|\W$|\W\W+|&',e)
r = re.sub
e = r("[ )(]", "", eval(dir()[0])[0])
return r("r|xx|^\W|\W$|\W\W|&|7x-", e, e.count('=') * e) == e
