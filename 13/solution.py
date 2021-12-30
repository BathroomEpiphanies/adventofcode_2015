import re
import sys

import itertools


likeability = {}
persons = set()
for line in sys.stdin.readlines():
    m = re.match(r'(?P<p1>\w+) would (?P<s>gain|lose) (?P<h>\d+) happiness units by sitting next to (?P<p2>\w+)',line).groupdict()
    persons.add(m['p1'])
    likeability[(m['p1'],m['p2'])] = int(m['h']) * (1 if m['s']=='gain' else -1)


def calculate_happiness(likeability,seating):
    return sum(likeability[(p1,p2)]+likeability[(p2,p1)] for p1,p2 in zip(seating,seating[1:]+(seating[0],)))


print('*1:',max(calculate_happiness(likeability,seating) for seating in itertools.permutations(persons)))

for person in persons:
    likeability[('Me',person)] = likeability[(person,'Me')] = 0
persons.add('Me')
print('*2:',max(calculate_happiness(likeability,seating) for seating in itertools.permutations(persons)))
