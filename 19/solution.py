import sys
import re
from itertools import count,product
from collections import defaultdict


#lines = [l.strip() for l in sys.stdin.readlines()]
#rules = defaultdict(list)
#for line in lines[:-2]:
#    i,o = line.split(' => ')
#    rules[i].append(tuple(re.findall(r'([A-Z][a-z]?)',o)))
#molecule = tuple(re.findall(r'([A-Z][a-z]?)',lines[-1]))
#
#
#inv_rules = {}
#for i,os in rules.items():
#    for o in os:
#        inv_rules[o] = (i,)
        
lines = [l.strip() for l in sys.stdin.readlines()]
#print(lines)
molecule = lines[-1][::-1]
#print(molecule)
reps = {
    o[::-1]:i[::-1] for i,o in [l.split(' => ') for l in lines[:-2]]
}
#reps = [
#    m for m in (re.findall(r'(\w+) => (\w+)',line) for line in lines[:-2])
#]
print(reps)
def rep(x):
    return reps[x.group()]

count = 0
while molecule != 'e':
    #print(molecule)
    molecule = re.sub('|'.join(reps.keys()), rep, molecule, 1)
    count += 1

print(f'*2: {count}')



exit()

import re

molecule = input.split('\n')[-1][::-1]
reps = {m[1][::-1]: m[0][::-1] 
        for m in re.findall(r'(\w+) => (\w+)', input)}
def rep(x):
    return reps[x.group()]

count = 0
while molecule != 'e':
    molecule = re.sub('|'.join(reps.keys()), rep, molecule, 1)
    count += 1

print(f'*2: {count}')
