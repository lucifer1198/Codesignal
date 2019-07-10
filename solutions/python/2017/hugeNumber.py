"""
Given an array of string numbers (i.e. strings that contain only digits),
return the greatest possible number of appending these numbers to each other as a string.

Example

For nums = [ "20", "3005", "2" ], the output should be
greatestNumber(nums) = "3005220".
"""

hugeNumber = lambda n: str(int(''.join(sorted(n, key=lambda n: n * 6)[::-1])))
