"""
Given a string equation, determine the value of x.

Example

For equation = "x = 4", the output should be
solveForX(equation) = 4.

For equation = "2*x = 21", the output should be
solveForX(equation) = 10.5.
"""

# solution by franciraldo
# def solveForX(e):
#    a, b = (eval(re.sub('=', '-(', e) + ')') for x in [0, 1])
#    return a / (a - b)

# solution by ernie_y
x = 1j
a = eval(re.sub('=', '-(', *eval(dir()[0])) + ')')
return -a.real / a.imag
