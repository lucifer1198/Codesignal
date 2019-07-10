"""
Given an undirected graph and some vertex index, find the size of the connected component of that vertex.

Example

For

matrix = [[false, true, false],
          [true, false, false],
          [false, false, false]]
and vertex = 0, the output should be
dfsComponentSize(matrix, vertex) = 2.

https://codefightsuserpics.s3.amazonaws.com/tasks/dfsComponentSize/img/ex.png
"""


def dfsComponentSize(m, v):
    S = [v]
    visited = [v]
    while len(S) != 0:
        c = S.pop()
        for i in range(len(m)):
            if not i in visited and m[i][v]:
                visited.append(i)
                S.append(i)
    return len(visited)
