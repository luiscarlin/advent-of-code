#!/usr/bin/env python3

'''
- region types = rocky, narrow, wet
- regions = X, Y (x and y >= 0)
- input: depth and coordinate of the target
- mouth of cave = (0, 0)
- geological index => erosion level

- to find geological index (follow the rule that first applies):
  - The region at 0,0 (the mouth of the cave) has a geologic index of 0.
  - The region at the coordinates of the target has a geologic index of 0.
  - If the region's Y coordinate is 0, the geologic index is its X coordinate times 16807.
  - If the region's X coordinate is 0, the geologic index is its Y coordinate times 48271.
  - Otherwise, the region's geologic index is the result of multiplying the erosion levels of the regions at X-1,Y and X,Y-1.

- to find erosion level:  A region's erosion level is its geologic index plus the cave system's depth, all modulo 20183. Then:

- to find region type:
  - If the erosion level modulo 3 is 0, the region's type is rocky.
  - If the erosion level modulo 3 is 1, the region's type is wet.
  - If the erosion level modulo 3 is 2, the region's type is narrow.

- risk levels: 0 for rocky regions, 1 for wet regions, and 2 for narrow regions.

- need to find risk level for the area where 0,0 and the target are at corners
'''
from collections import defaultdict

def find_index(row, col, target_r, target_c, erosion_levels):
  if (row, col) is (0, 0):
    return 0

  if (row, col) is (target_r, target_c):
    return 0

  if col is 0:
    return row * 16807

  if row is 0:
    return col * 48271

  return erosion_levels[(row-1, col)] * erosion_levels[(row, col-1)]

def get_erosion_level(index, cave_depth):
  return (index + cave_depth) % 20183

def get_region_type(erosion_level):
  types = ['r', 'w', 'n']

  idx = erosion_level % 3

  return types[idx]

cave_depth = 11394

target_r = 7
target_c = 701

mouth = (0, 0)

erosion_levels = defaultdict(int)

risk_levels = {
  'r': 0,
  'w': 1,
  'n': 2
}

risk = 0

for row in range(target_r + 1):
  for col in range(target_c + 1):

    index = find_index(row, col, target_r, target_c, erosion_levels)

    erosion_level = get_erosion_level(index, cave_depth)
    erosion_levels[(row, col)] = erosion_level

    region_type = get_region_type(erosion_level)

    risk += risk_levels[region_type]

print('part 1', risk)