import re
import sys

import numpy as np
import itertools


ingredients = []
values = []
for line in sys.stdin.readlines():
    m = re.match(r'(?P<name>\w+): capacity ([-\d]+), durability ([-\d]+), flavor ([-\d]+), texture ([-\d]+), calories ([-\d]+)',line).groups()
    ingredients.append(m[0])
    values.append(m[1:])
#print(values)
values = np.array(values,int)


#print(ingredients)
#print(values)
#print()


def score_recipie(values,mix):
    val = (mix*values).sum(axis=0)
    val[val<0] = 0
    return val[:-1].prod(),val[-1]
    
maxscore = 0
for mix in (np.array([(i,j,k,100-i-j-k)]).T for i in range(0,100) for j in range(100-i) for k in range(100-i-j)):
#for mix in (np.array([(i,100-i)]).T for i in range(0,100)):
    score,_ = score_recipie(values,mix)
    if score > maxscore:
        maxscore = score
        #print(mix.T,maxscore)
print('*1:',maxscore)


maxscore = 0
for mix in (np.array([(i,j,k,100-i-j-k)]).T for i in range(0,100) for j in range(100-i) for k in range(100-i-j)):
#for mix in (np.array([(i,100-i)]).T for i in range(0,100)):
    score,calories = score_recipie(values,mix)
    if score > maxscore and calories==500:
        maxscore = score
        #print(mix.T,maxscore)
print('*2:',maxscore)
