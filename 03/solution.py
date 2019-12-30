import sys

deltas = {
    '>': ( 1, 0),
    '^': ( 0, 1),
    '<': (-1, 0),
    'v': ( 0,-1),
    '\n':( 0, 0)
}
def add(a,b):
    return (a[0]+b[0],a[1]+b[1])


directions = sys.stdin.readline()

houses = set()
pos = (0,0)
for d in directions:
    houses.add( pos )
    pos = add( pos , deltas[d] )

print( f"*1: {len(houses)}" )

santa = set()
spos = (0,0)
robot = set()
rpos = (0,0)
for i,d in enumerate(directions):
    if i%2 == 0:
        santa.add( spos )
        spos = add( spos , deltas[d] )
    else:
        robot.add( rpos )
        rpos = add( rpos , deltas[d] )

print( f"*2: {len(santa | robot)}" )
