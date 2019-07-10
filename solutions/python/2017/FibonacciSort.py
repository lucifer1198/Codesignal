# Best Solution by: https://codefights.com/profile/eibe
# Question: https://python.web.id/blog/fibonaccisort-cf/

def FibonacciSort(s):
    f = [0]
    i = j = 1
    while j < len(s):
        i , j = j, i + j
        f += [i]
    for i, j in zip(f, sorted(s[i] for i in f)):
        s[i] = j
    return s
