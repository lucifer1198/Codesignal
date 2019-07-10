"""
Forrest Gump runs in a circle shaped road. Because he will run too much, he wants to have breaks several times.
He loves shrimp too much, so he wants to eat shrimps to recover his energy. There is n restaurants on that road where Forrest will have breaks.
Running one mile he uses 1 unit of energy and eating 1 shrimp he recovers 1 unit of energy. At the start Forrest have 0 units of energy.
Units of energy he have can not be negative. Now he wants to know where to start to have enough energy to run one lap.

Example

For dist = [1, 2, 3] and shrimp = [1, 2, 3], the output should be
runForerstRun(dist, shrimp) = 1.

All three points satisfy the condition so the minimal one is the answer.

For dist = [1, 1, 1] and shrimp = [0, 0, 3], the output should be
runForerstRun(dist, shrimp) = 3.

If he starts from 1st or 2nd restaurant, he can't run, because he have no energy.
So he starts from 3rd one, fills his energy to 3 units and runs whole circle.
"""

# solution by cifko
e = j = 1
for d, s in zip(*eval(dir()[0])):
    if e < 2:
        R = j
        e = 2
    e += s - d
    j += 1
return R
