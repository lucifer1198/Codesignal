"""
Consider several points lying on a straight line. Call an unordered triple of points an equidistant triple if one of them is the mid-point of the segment formed by the other two.

Given the coordinates of the points, find the number of equidistant triples formed by them.

Example

For coordinates = [1, 2, 4, 6, 7, 8], the output should be
equidistantTriples(coordinates) = 4.

The equidistant triples are: (1, 4, 7), (2, 4, 6), (4, 6, 8), (6, 7, 8).

Check out the image below for better understanding:

https://codefightsuserpics.s3.amazonaws.com/tasks/equidistantTriples/img/example.png
"""


def equidistantTriples(coordinates):
    ans = 0
    for i in range(len(coordinates)):
        left = i - 1
        right = i + 1
        while (left >= 0 and right < len(coordinates)):
            distL = coordinates[i] - coordinates[left]
            distR = coordinates[right] - coordinates[i]
            if distL == distR:
                ans += 1
                left -= 1
                right += 1
            elif distL < distR:
                left -= 1
            else:
                right += 1
    return ans
