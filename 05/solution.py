import re
import sys

from collections import defaultdict

input_ = [ x.strip() for x in sys.stdin.readlines() ]

nice = 0
for line in input_:
    #line = line[0:-1]
    counts = defaultdict(lambda:0)
    counts.update( { line[0] : 1 } )
    for i in range(1,len(line)):
        a = line[i]
        b = line[i-1:i+1]
        counts.update( { a : counts[a]+1 } )
        counts.update( { b : counts[b]+1 } )

    vowels = sum( [ counts[x] for x in ['a','e','i','o','u'] ] )
    demand = any( map( lambda x: x in counts , ['aa','bb','cc','dd','ee','ff','gg','hh','ii','jj','kk','ll','mm',
                                                'nn','oo','pp','qq','rr','ss','tt','uu','vv','ww','xx','yy','zz'] ) )
    forbid = any( map( lambda x: x in counts , ['ab','cd','pq','xy'] ) )

    #print( vowels )
    #print( demand )
    #print( forbid )
    if vowels >=3 and demand and not forbid:
        nice += 1
        #print( line )
    
print( f"*1: {nice}" )


alphabet = "abcdefghijklmnopqrstuvwxyz"

nice = 0
for line in input_:
    double = False
    repeat = False
    for a in alphabet:
        if re.findall( f'{a}.{a}' , line):
            repeat = True
        for b in alphabet:
            if len(re.findall( f'{a}{b}' , line)) >= 2:
                double = True
    #if double:
    #    print( f"{a}{b} found in {line}" )
    #if repeat:
    #    print( f"{a}_{a} found in {line}" )
        
    if double and repeat:
        nice += 1
        #print( line )

print( f"*2: {nice}" )
