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

directions = {
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
root_stack = []

for idx, char in enumerate(line):
  if char is '(':
    root_stack.append((curr_r, curr_c))
  elif char is '|':
    if line[idx + 1] == ')':
      curr_r, curr_c = root_stack.pop()
    else:
      curr_r, curr_c = root_stack[-1]
  elif char is ')' and line[idx - 1] is not '|':
    root_stack.pop()
  elif char in 'NSEW':
    prev_r = curr_r
    prev_c = curr_c

    curr_r += dr[directions[char]]
    curr_c += dc[directions[char]]

    G.add_edge((prev_r, prev_c), (curr_r, curr_c))


# find shortest to every node (going through nodes once)
lengths = nx.algorithms.shortest_path_length(G, origin)

print('part 1', max(lengths.values()))
print('part 2', sum(1 for length in lengths.values() if length >= 1000))
