import sys
import itertools
from collections import namedtuple

character = namedtuple('Character',['hp','dmg','arm'])

weapons = [       # Cost Damage  Armor
    ('Dagger',         8,     4,     0),
    ('Shortsword',    10,     5,     0),
    ('Warhammer',     25,     6,     0),
    ('Longsword',     40,     7,     0),
    ('Greataxe',      74,     8,     0),
]

armor = [         # Cost Damage  Armor
    ('Naked',          0,     0,     0),
    ('Leather',       13,     0,     1),
    ('Chainmail',     31,     0,     2),
    ('Splintmail',    53,     0,     3),
    ('Bandedmail',    75,     0,     4),
    ('Platemail',    102,     0,     5),
]

rings = [         # Cost Damage  Armor
    ('None 1',         0,     0,     0),
    ('None 2',         0,     0,     0),
    ('Damage +1',     25,     1,     0),
    ('Damage +2',     50,     2,     0),
    ('Damage +3',    100,     3,     0),
    ('Defense +1',    20,     0,     1),
    ('Defense +2',    40,     0,     2),
    ('Defense +3',    80,     0,     3),
]


boss = character(*[int(l.strip().split(': ')[1]) for l in sys.stdin.readlines()])


def fight(plyr,boss):
    while True:
        boss = character(boss.hp-max(1,plyr.dmg-boss.arm),boss.dmg,boss.arm)
        if boss.hp <= 0:
            return True
        plyr = character(plyr.hp-max(1,boss.dmg-plyr.arm),plyr.dmg,plyr.arm)
        if plyr.hp <= 0:
            return False


cheapest = float('inf')
for w,a,(r1,r2) in itertools.product(weapons,armor,itertools.combinations(rings,2)):
    cost = sum(i[1] for i in [w,a,r1,r2])
    dmg = sum(i[2] for i in [w,a,r1,r2])
    arm = sum(i[3] for i in [w,a,r1,r2])
    plyr = character(100,dmg,arm)
    if cost<cheapest and fight(plyr,boss):
        cheapest = cost
        #print(w,a,r1,r2,cost)
print('*1:',cheapest)


expensivest = 0
for w,a,(r1,r2) in itertools.product(weapons,armor,itertools.combinations(rings,2)):
    cost = sum(i[1] for i in [w,a,r1,r2])
    dmg = sum(i[2] for i in [w,a,r1,r2])
    arm = sum(i[3] for i in [w,a,r1,r2])
    plyr = character(100,dmg,arm)
    if cost>expensivest and not fight(plyr,boss):
        expensivest = cost
        #print(w,a,r1,r2,cost)
print('*2:',expensivest)

