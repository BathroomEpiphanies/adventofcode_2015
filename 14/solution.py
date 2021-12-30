import re
import sys

from collections import namedtuple


Stats = namedtuple('Stats',['speed','dash','rest'])

raindeers = {}
for line in sys.stdin.readlines():
    m = re.match(r'(?P<name>\w+) can fly (?P<speed>\d+) km/s for (?P<dash>\d+) seconds, but then must rest for (?P<rest>\d+) seconds.',line).groupdict()
    raindeers[m['name']] = Stats(int(m['speed']),int(m['dash']),int(m['rest']))


def distance(stats,duration):
    return stats.speed * (duration//(stats.dash+stats.rest)*stats.dash + min(duration%(stats.dash+stats.rest),stats.dash))
    

duration = 2503

distances = sorted([(distance(stats,duration),name) for name,stats in raindeers.items()])
print(distances[-1], file=sys.stderr)
print('*1:',distances[-1][0])

scores = {deer:0 for deer in raindeers}
for split in range(1,duration+2):
    distances = sorted([(distance(stats,split),name) for name,stats in raindeers.items()])
    scores[distances[-1][1]] += 1
scores = sorted((s,d) for d,s in scores.items())
print(scores[-1], file=sys.stderr)
print('*2:',scores[-1][0])
