import itertools
import sys

numbers = sys.stdin.readlines()[0].strip()

for i in range(1,51):
    numbers = ''.join(f'{len(list(g))}{k}' for k,g in itertools.groupby(numbers))
    if i == 40:
        print(f'*1: {len(numbers)}')
    if i == 50:
        print(f'*2: {len(numbers)}')

