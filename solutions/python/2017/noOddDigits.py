"""
Given a non-negative integer number, remove all of its odd digits (if all of the digits are removed, return zero).
"""

# answer by kolapsys
noOddDigits = lambda n: int(re.sub('[13579]','','0'+str(n)))

>>> noOddDigits(12345678)
2468
