import sys
import itertools
import functools
import operator


values = [int(l) for l in sys.stdin.readlines()]


def find_minimum_configuration(packages,bins):
    target_weight = sum(packages)//bins
    minimum_config = (float('inf'),None)
    for size in range(len(packages)):
        for config in (c for c in itertools.combinations(packages,size) if sum(c)==target_weight):
            minimum_config = min(minimum_config,(functools.reduce(operator.mul,config),config))
        if minimum_config[1]:
            return minimum_config


entanglement,configuration = find_minimum_configuration(values,3)
print(entanglement,configuration, file=sys.stderr)
print('*1:',entanglement)

entanglement,configuration = find_minimum_configuration(values,4)
print(entanglement,configuration, file=sys.stderr)
print('*2:',entanglement)
