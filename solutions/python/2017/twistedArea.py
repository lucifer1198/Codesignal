"""
A string consisting of the letters n, e, s, and w can be interpreted 
as a path by taking each letter as an instruction to move one unit north, east, south, or west. 
A path is said to be closed if it starts and ends at the same point.

Your task is to write a function twistedArea that takes a closed path 
and returns the area enclosed by the path. The twist is that squares 
that the path winds around in a counterclockwise direction are counted positively, 
but squares that the path winds around in a clockwise direction are counted negatively. 
More precisely, the twistedArea of a closed path is the sum of the winding numbers of the squares enclosed by the path.

Example

For path = "eeennwsssswnnneeennwwwwsss", the output should be
twistedArea(path) = 9.
The path starts and ends at the red dot and is shown in blue in the image below. 
The winding number for each square is shown in the center of the square, and the sum of the winding numbers is 9.

https://i.imgur.com/YDBwVSf.png

For path = "nsew" the output should be
twistedArea(path) = 0.
The path doesn't wind around any squares.

For path consisting of 10,000 repetitions of "n" followed by 20,000 repetitions of "e" followed by 10,000 repetitions of "sww", 
the output should be -100010000. The path makes a roughly triangular shape containing 100010000 squares. 
The path winds around each of the enclosed squares in a clockwise direction, 
so the winding number for each square is -1 and the sum of the winding numbers is -100010000.
"""

# solution by: william_c43
def twistedArea(p):
    #integral trick here
    #basically d(x dy)=dx wedge dy
    #then use stokes
    x=0
    a=0
    for c in p:
        if c is 'e': x+=1
        if c is 'w': x-=1
        if c is 'n': a+=x
        if c is 's': a-=x
    return a


# solution by: ernie_y
# This just Green's Theorem
# https://en.wikipedia.org/wiki/Green%27s_theorem
# I use Green's Theorem to help me think about path intetral
# I set L = y and M = 0 
# And the area will be equal to path integral -ydx
# However, it actually doesn't require the whole Green theorem 
# we just need to know a area under a curve is xdy or ydx
# if the paht is closed this integral will be equal to the twistedArea
# 
#def twistedArea(p):
#    y = a = 0 
#    for i in p:
#        y+='ewn'.find(i)/2
#        a+='nsw'.find(i)/2*y
#    return a
#def twistedArea(p):
y = a = 0 
for i in eval(dir()[0])[0]:
    k = ' e s n w'.find(i)
    y+= k%3-1
    a+= k/3*y-y
return a
