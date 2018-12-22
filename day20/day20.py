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
import matplotlib.pyplot as plt
from collections import deque, defaultdict

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

G = nx.Graph()

line = open('input.txt').read()[1:-1]

curr_r = curr_c = 0

origin = (curr_r, curr_c)

some_stack = []

for i, char in enumerate(line):
  if char is '(':
    some_stack.append((curr_r, curr_c))
    continue

  if char is '|' and line[i + 1] == ')':
    curr_r, curr_c = some_stack.pop()
    continue

  if char is '|':
    curr_r, curr_c = some_stack[-1]
    continue

  if char is ')' and line[i - 1] is not '|':
    some_stack.pop()
    continue

  if char in 'NSEW':
    prev_r = curr_r
    prev_c = curr_c

    direction = dir[char]

    curr_r += dr[direction]
    curr_c += dc[direction]

    G.add_edge((prev_r, prev_c), (curr_r, curr_c))

lengths = nx.algorithms.shortest_path_length(G, origin)
print('part1:', max(lengths.values()))
print('part2:', sum(1 for length in lengths.values() if length >= 1000))
