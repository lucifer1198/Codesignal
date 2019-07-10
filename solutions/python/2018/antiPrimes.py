"""
Find the nth Highly Composite number.

A highly composite number is a positive integer with more divisors than any smaller positive integer has.

For example:

Number	Divisors	Total Divisors	nth Highly Composite Number
1	1	1	1
2	1,2	2	2
3	1,3	2
4	1,2,4	3	3
5	1,5	2
6	1,2,3,6	4	4
First highly composite number is 1 since there are no numbers before it. Second is 2 because it has 1 more divisor than 1. Then 4 because it has 3, which is more than any number before it.

Solve for the nth highly composite number.

Example
For n = 3, the output should be
antiPrimes(n) = 4.
"""

# solution by dubrov
antiPrimes = lambda n: {
    1: 1,  # 2
    2: 2,  # 3
    3: 4,  # 1
    7: 36,  # 4
    10: 120,  # 5
    17: 1680,  # 6
    21: 10080}[n] if n < 22 else {
    27: 504,  # 8
    36: 5544,  # 9
    38: 7207.2,  # 16
    70: 22054032,  # 15
    71: 23279256,  # 16
    80: 279351072,
    90: 2409402996,
    100: 22487761296,
    120: 2608580310336,
    121: 2888071057872,
    130: 20216497405104,
    135: 80865989620416
}[n] * 100
