#!/usr/bin/env python3

from collections import defaultdict
import networkx as nx

rocky, wet, narrow = 0, 1, 2
torch, climbing_gear, neither = 0, 1, 2
allowed_items = { rocky: (torch, climbing_gear), wet: (climbing_gear, neither), narrow: (torch, neither) }

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

def populate_cave_map(depth, corner, target):
  grid = {}

  for row in range(0, corner[0] + 1):
    for col in range(0, corner[1] + 1):
      if (row, col) in [(0, 0), target]:
        index = 0
      elif col is 0:
        index = row * 16807
      elif row is 0:
        index = col * 48271
      else:
        index = grid[(row - 1, col)][1] * grid[(row, col - 1)][1]

      erosion_level = (index + depth) % 20183
      risk = erosion_level % 3
      grid[(row, col)] = (index, erosion_level, risk)

  return grid

def part1():
  cave_depth = 11394

  target_r = 7
  target_c = 701

  erosion_levels = defaultdict(int)

  risk = 0

  for row in range(target_r + 1):
    for col in range(target_c + 1):

      index = find_index(row, col, target_r, target_c, erosion_levels)

      erosion_level = get_erosion_level(index, cave_depth)
      erosion_levels[(row, col)] = erosion_level

      region_type = erosion_level % 3

      risk += region_type

  print('part 1', risk)

def part2():
  cave_depth = 11394
  target = (7, 701)
  corner = (target[0] + 100, target[1] + 100)

  cave = populate_cave_map(cave_depth, corner, target)

  grid = {coord: values[2] for coord, values in (cave).items()}
  graph = create_graph(grid, corner, target)

  shortest_weighted_distance = nx.dijkstra_path_length(graph, (0, 0, torch), (*target, torch))

  print('part 2', shortest_weighted_distance)

def create_graph(grid, corner, target):
  graph = nx.Graph()
  for row in range(corner[0] + 1):
    for col in range(corner[1] + 1):
      items = allowed_items[grid[(row, col)]]
      graph.add_edge((row, col, items[0]), (row, col, items[1]), weight = 7)
      for d_r, d_c in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        new_row, new_col = row+d_r, col+d_c

        if 0 <= new_row <= corner[0] and 0 <= new_col <= corner[1]:
          new_items = allowed_items[grid[(new_row, new_col)]]
          for item in set(items).intersection(set(new_items)):
            graph.add_edge((row, col, item), (new_row, new_col, item), weight = 1)
  return graph

def get_weighted_graph(grid, target, corner):
  G = nx.Graph()

  for row in range(corner[0] + 1):
    for col in range(corner[1] + 1):
      region_type = grid[(row, col)]

      items = allowed_items[region_type]

      G.add_edge((row, col, items[0]), (row, col, items[1]), weight = 7)

      for (dr, dc) in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
        new_row = row + dr
        new_col = col + dc

        if 0 <= new_row <= corner[0] and 0 <= new_col <= corner[1]:
          new_region_type = grid[(new_row, new_col)]
          new_items = allowed_items[new_region_type]

          common_items = set(new_items).intersection(set(items))

          for item in common_items:
            G.add_edge((row, col, item), (new_row, new_col, item), weight = 1)

  return G

def main():
  part1()
  part2()

if __name__ == '__main__':
  main()
