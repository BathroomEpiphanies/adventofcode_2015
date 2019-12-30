import sys

directions = sys.stdin.read()

floor = 0
basement = None
for p,i in enumerate(directions):
    if   i == '(':
        floor += 1
    elif i == ')':
        floor -= 1
    if floor < 0 and basement is None:
        basement = p+1

print( f"*1: {floor}" )
print( f"*2: {basement}" )
