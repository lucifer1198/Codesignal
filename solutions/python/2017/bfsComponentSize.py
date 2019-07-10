"""
Given the adjacency matrix of an undirected graph with no loops or multiple edges, find the size of the connected component of vertex 1 (0-based).

Example

For

matrix = [[false, true, false],
          [true, false, false],
          [false, false, false]]
the output should be
bfsComponentSize(matrix) = 2.

The component contains vertices 0 and 1.



For

matrix = [[false, false, true, false],
          [false, false, false, false],
          [true, false, false, true],
          [false, false, true, false]]
the output should be
bfsComponentSize(matrix) = 1.

The component consists of a single vertex 1.
"""


def bfsComponentSize(matrix):
    visited = [False for i in range(len(matrix))]
    queue = []
    componentSize = 0

    visited[1] = True
    queue.append(1)
    while len(queue) > 0:
        currentVertex = queue.pop()
        visited[currentVertex] = True
        componentSize += 1
        for nextVertex in range(len(matrix)):
            if matrix[currentVertex][nextVertex] and not visited[nextVertex]:
                visited[nextVertex] = True
                queue.append(nextVertex)

    return componentSize
