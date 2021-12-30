import sys

from sympy.ntheory import divisors
import itertools


number = int(sys.stdin.readlines()[0])


def handout10(house):
    return 10*sum(divisors(house))

for house,presents in ((i,handout10(i)) for i in itertools.count(1)):
    #print(house,presents)
    if presents>=number:
        break
print('*1:',house)


def handout11(house):
    return 11*sum(n for n in divisors(house) if house<=n*50)

for house,presents in ((i,handout11(i)) for i in itertools.count(1)):
    #print(house,presents)
    if presents>=number:
        break
print('*2:',house)
