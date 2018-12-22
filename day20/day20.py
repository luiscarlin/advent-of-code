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

def dead_ends(G, source):

  visited = set()
  visited.add(source)

  q = deque()
  q.append(source)

  prev = defaultdict(tuple)

  dead_ends = []

  while q:
    node = q.popleft()

    neighbors = list([n for n in G.neighbors(node)])
    neighbors.sort()

    dead_end = True

    for next in neighbors:
      if next not in visited:
        dead_end = False
        q.append(next)
        visited.add(next)
        prev[next] = node

    if dead_end:
      dead_ends.append(node)

  return dead_ends

  # path = []
  # path.append(target)
  # parent = prev[target]

  # while parent:
  #   path.append(parent)
  #   parent = prev[parent]

  # path.reverse()

  # if path[0] == source:
  #   return path
  # else:
  #   return []

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
# line = '^WNE$'[1:-1] # 3
# line = '^ENWWW(NEEE|SSE(EE|N))$'[1:-1]  # 10
# line = 'WNE(NN|E)'
# line = '^ENNWSWW(NEWS|)SSSEEN(WNSE|)EE(SWEN|)NNN$'[1:-1] #18s

curr_r = curr_c = 0

origin = (curr_r, curr_c)

some_stack = []
# possible_ends = []

for i, char in enumerate(line):

  # if char is '$':
  #   possible_ends.append((curr_r, curr_c))
  #   continue
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

# print(G.nodes)
# nx.draw(G)

# leaves = [x for x in G.nodes() if G.out_degree(x)==0 and G.in_degree(x)==1]
# print('leaves', leaves)

# min_distance = 1e7
# for leaf in leaves:
#   path = nx.shortest_path(G, (0, 0), leaf)

#   if len(path) < min_distance:
#     min_distance = len(path)

# print(min_distance - 1)

# for path in nx.all_simple_paths(G, source=0, target=3):
#   print(path)

ends = dead_ends(G, origin)

all_paths = []
for end in ends:
  path = nx.shortest_path(G, (0, 0), end)
  all_paths.append(path)
  # print(path)

most_doors = len(max(all_paths, key = lambda path: len(path))) - 1

print('most doors', most_doors)
# nx.draw(G, node_size = 20, with_labels = True)
# plt.show()


# print(len(path) -1)
# print('min path distance', min_distance)
# print('number of doors', min_distance - 1)

# min_distance = len(G)
# min_distance = 1e7
# for poss_end in possible_ends:
#   path = nx.shortest_path(G, (0, 0), poss_end)
#   distance = len(path)

#   if distance < min_distance:
#     min_distance = distance


# print('min path distance', min_distance)
# print('number of doors', min_distance - 1)

