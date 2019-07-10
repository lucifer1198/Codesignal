"""
Your notoriously Grinchy office has decided to get into the holiday spirit this year.
They want to make the bulletin boards Christmas-themed so they covered them with red paper. This does come with some rules though.

* Any paper placed on a red background must be colored green;
* Any paper placed on a green background must be colored red;
* You can have nested backgrounds if you wish (e.g. you can have a red paper placed on top of a green paper that is placed on the red bulletin board;
* Any paper you place on another cannot completely cover the background in width, height, or both;
* You cannot overlap papers on the same background.
* You like red and want to figure out if any given bulletin board has more (or equal) red than green.

You are given a matrix of integers. Each array represents a box on the bulletin board. Each array has the following 4 values (in order):

1. The box's id;
2. The box's width;
3. The box's height;
4. The box's parent's id.

A box's "parent" is the box that it is placed on top of. Note: the position of the child boxes within the parent box does not matter.
There can be multiple boxes with the same parent, but the boxes will not overlap.

The outermost box will have a parent id of 0 and will be red. The child of a red box will be green and the child of a green box will be red.

Given this, determine whether there is more visible red area than green.

Example
For input = [[1, 5, 5, 0], [2, 3, 4, 1]]

the output should be

isMoreRed(input) = true.

The outermost box is red and has an area of 25. That box is then covered by a green box that has an area of 12.
That means the total visible area is 13 for red and 12 for green.
"""


def isMoreRed(i):
    # solution by ernie_y
    A = [0] * 9999
    for a, b, c, d in i[::-1]:
        A[d] += b * c - A[a]
    return A[0] > A[1]
