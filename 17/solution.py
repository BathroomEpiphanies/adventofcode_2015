import sys

import itertools
import numpy as np

from collections import defaultdict


containers = np.array(sorted([int(l) for l in sys.stdin.readlines()]))


combinations = defaultdict(list)
for m in itertools.product([0,1],repeat=len(containers)):
    m = np.array(m)
    v = containers.dot(m)
    if v==150:
        combinations[m.sum()].append(''.join(str(d) for d in m))

print('*1:',sum(len(v) for v in combinations.values()))
print('*2:',len(combinations[sorted(combinations.keys())[0]]))
