import cv2
import re
import sys

import numpy as np


instructions = [l.strip() for l in sys.stdin.readlines()]


lights = np.zeros((1000,1000),dtype=int)
for instruction in instructions:
    m = re.match(r'(?P<action>.+) (?P<x1>[0-9]+),(?P<y1>[0-9]+) through (?P<x2>[0-9]+),(?P<y2>[0-9]+)',instruction)
    x1,x2,y1,y2 = (int(m[i]) for i in ['x1','x2','y1','y2'])
    x2 += 1
    y2 += 1
    if m['action'] == 'turn on':
        lights[y1:y2,x1:x2] = 1
    elif m['action'] == 'turn off':
        lights[y1:y2,x1:x2] = 0
    elif m['action'] == 'toggle':
        lights[y1:y2,x1:x2] = 1-lights[y1:y2,x1:x2]

print(f'*1: {np.sum(lights)}')
#cv2.imwrite('debug_1.png',127*lights)


lights = np.zeros((1000,1000),dtype=int)
for instruction in instructions:
    m = re.match(r'(?P<action>.+) (?P<x1>[0-9]+),(?P<y1>[0-9]+) through (?P<x2>[0-9]+),(?P<y2>[0-9]+)',instruction)
    x1,x2,y1,y2 = (int(m[i]) for i in ['x1','x2','y1','y2'])
    x2 += 1
    y2 += 1
    if m['action'] == 'turn on':
        lights[y1:y2,x1:x2] += 1
    elif m['action'] == 'turn off':
        lights[y1:y2,x1:x2] -= 1
        lights[lights<0] = 0
    elif m['action'] == 'toggle':
        lights[y1:y2,x1:x2] += 2

print(f'*2: {np.sum(lights)}')
#cv2.imwrite('debug_2.png',lights)
