import sys

import numpy as np
import cv2


grid_orig = np.array([[p=='#' for p in l.strip()] for l in sys.stdin.readlines()],'uint8')


def update(grid,always):
    neighbor = cv2.filter2D(grid,-1,np.array(((1,1,1),(1,0,1),(1,1,1))),borderType=cv2.BORDER_ISOLATED)
    return (grid & (1<neighbor) & (neighbor<4)) | (~grid & neighbor==3) | always


grid = grid_orig.copy()
for i in range(100):
    grid = update(grid,0)
print('*1:',grid.sum())


corners = np.zeros_like(grid_orig)
corners[0,0] = corners[-1,0] = corners[0,-1] = corners[-1,-1] = 1
grid = grid_orig.copy() | corners
for i in range(100):
    grid = update(grid,corners)
print('*2:',grid.sum())
