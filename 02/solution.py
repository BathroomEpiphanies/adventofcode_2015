import sys

paper = 0
ribbon = 0
for line in sys.stdin.readlines():
    a,b,c = [ int(x) for x in line.split('x') ]
    A_ab = a*b
    A_bc = b*c
    A_ac = a*c
    A = 2*A_ab + 2*A_bc + 2*A_ac + min(A_ab,A_bc,A_ac)
    paper += A

    V = a*b*c
    O_ab = 2*(a+b)
    O_bc = 2*(b+c)
    O_ac = 2*(a+c)

    ribbon += V + min(O_ab,O_bc,O_ac)
    
print( f"*1: {paper}" )
print( f"*2: {ribbon}" )
