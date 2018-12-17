#!/usr/bin/env python3

import sys
from collections import deque, defaultdict
import networkx as nx

ELF_TYPE = 'E'
GOBLIN_TYPE = 'G'

class Unit:
  def __init__(self, row, col, unit_type):
    self.row = row
    self.col = col
    self.unit_type = unit_type
    self.attack_power = 3
    self.hit_points = 200
    self.is_alive = True

  def get_coords(self):
    return (self.row, self.col)

  def __str__(self):
    return self.unit_type

def main():
  cave, units = parse_input()

  G = generate_graph(cave)

  print('initial state')
  show_all(cave, units)

  round = 0
  all_enemies_dead = False

  while not all_enemies_dead:
    print('starting round')

    # remove this later
    if round == 5:
      break

    units = sorted(units, key = lambda unit: unit.get_coords())

    for current_unit in units:

      if not current_unit.is_alive:
        continue

      enemies = [other for other in units if other.unit_type != current_unit.unit_type and other.is_alive]

      if not enemies:
        print('game over. All your enemies are dead')
        all_enemies_dead = True
        break

      current_unit_neighbors = get_neighbors(*current_unit.get_coords())
      print('current unit neighbors', current_unit_neighbors)

      enemies_in_range = [enemy for enemy in enemies if enemy.get_coords() in current_unit_neighbors]
      print('enemies in range', enemies_in_range)

      if enemies_in_range:
        # TODO implement attack and call it
        print('attack')
      else:
        move(G, current_unit, units, enemies )
    round += 1
    print('end of round', round)
    show_all(cave, units)

def move(G, current_unit, units, enemies ):
  source = current_unit.get_coords()
  target_list = [enemy.get_coords() for enemy in enemies]
  blockers = [unit.get_coords() for unit in units if unit.is_alive]

  enemy_paths = find_shortest_path_to_enemies(G, source, blockers, target_list)
  print('moving')

def find_shortest_path_to_enemies(G, source, blockers, target_list):
  print('get paths to enemies')


  for target in target_list:
    path = bfs(G, source, blockers, target)

def bfs(G, source, blockers, target):
  visited = set()
  visited.add(source)

  q = deque()
  q.append(source)

  prev = defaultdict(int)

  while q:
    node = q.popleft()

    neighbors = [n for n in G.neighbors(node)]
    neighbors = sorted(neighbors)

    for next in neighbors:
      if next not in visited and next not in blockers:
        q.append(next)
        visited.add(next)
        prev[next] = node

  path = []
  parent = prev[target]

  while parent != 0:
    path.append(parent)
    parent = prev[parent]

  path.reverse()
  return path

def show_all(cave, units):
  for row in range(len(cave)):
    for col in range(len(cave[row])):

      unit_in_spot = False

      for unit in units:
        if unit.row == row and unit.col == col:
          print(unit, end = '')
          unit_in_spot = True
          break

      if not unit_in_spot:
        print(cave[row][col], end = '')
    print()

def parse_input():
  cave = []
  units = []

  for line in open('input.txt'):
    cave.append([c for c in line.strip()])

  for row in range(len(cave)):
    for col in range(len(cave[row])):
      if cave[row][col] == GOBLIN_TYPE:
        units.append(Unit(row, col, GOBLIN_TYPE))
        cave[row][col] = '.'
      elif cave[row][col] == ELF_TYPE:
        units.append(Unit(row, col, ELF_TYPE))
        cave[row][col] = '.'
  return cave, units

def show_units(units):
  for unit in units:
    print("{} at {} with attack power={} and hit points={}".format(unit, unit.get_coords(), unit.attack_power, unit.hit_points))

def generate_graph(cave):
  G = nx.Graph()

  for row in range(len(cave)):
    for col in range(len(cave[row])):
      if cave[row][col] == ".":
        neighbors = get_neighbors(row, col)

        for (r, c) in neighbors:
          if 0 <= r < len(cave) and 0 <= c < len(cave[r]):
            if cave[r][c] == '.':
              G.add_edge((row, col), (r, c))
  return G

def get_neighbors(x, y):
  # up , down, left, right
  directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
  return list(map(lambda direction: (x + direction[0], y + direction[1]), directions))

if __name__ == '__main__':
  main()
