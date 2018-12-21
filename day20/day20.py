#!/usr/bin/env python3
'''
- rooms = .
- walls = #
- doors = - or |
- current position = X
- routes will take you through every door

^N(E|W)N$
N => E => N
  => W => N

^ENWWW(NEEE|SSE(EE|N))$
E => N => W => W => W => N => E => E => E
                      => S => S => E => E => E
                                     => N

(NEWS|WNSE|) = take it or skip it
find the room for which the shortest path to that room would require passing through the most doors.

'''

import networkx as nx

# up, right, down, left
# up = 0
# right = 1
# down = 2
# left = 3
dir = {
  'N': 0,
  'E': 1,
  'S': 2,
  'W': 3
}

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

# line = open('input.txt').read()[1:-1]
line = '^WNE$'[1:-1]

curr_r = curr_c = 0

for char in line:
  direction = dir[char]

  curr_r += dr[direction]
  curr_c += dc[direction]



  print(char)