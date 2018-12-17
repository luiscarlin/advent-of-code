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

  def set_pos(self, row, col):
    self.row = row
    self.col = col

  def attacked_with_power(self, power):
    self.hit_points -= power
    if self.hit_points <= 0:
      self.is_alive = False

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

      enemies_in_range = [enemy for enemy in enemies if enemy.get_coords() in current_unit_neighbors]

      if enemies_in_range:
        attack(current_unit, enemies_in_range)
      else:
        move(G, current_unit, units, enemies)

    round += 1
    print('end of round', round)
    show_all(cave, units)

def attack(current_unit, enemies_in_range):
  enemy_to_attack = min(enemies_in_range, key = lambda enemy: enemy.hit_points)

  enemy_to_attack.attacked_with_power(current_unit.attack_power)

def move(G, current_unit, units, enemies ):
  source = current_unit.get_coords()
  target_list = [enemy.get_coords() for enemy in enemies]
  blockers = [unit.get_coords() for unit in units if unit.is_alive]

  enemy_path = find_shortest_path(G, source, blockers, target_list)

  if enemy_path:
    next_step = enemy_path[1:][0]
    current_unit.set_pos(*next_step)

def find_shortest_path(G, source, blockers, target_list):
  paths_to_all_enemies = []

  for target in target_list:
    paths_to_all_enemies.append(bfs(G, source, blockers, target))

  distances = [len(path) for path in paths_to_all_enemies]

  min_distance = min(distances)

  min_distance_paths = [path for path in paths_to_all_enemies if len(path) == min_distance]

  if len(min_distance_paths) == 1:
    return min_distance_paths[0]

  return min(min_distance_paths)

def bfs(G, source, blockers, target):
  blockers.remove(target)

  visited = set()
  visited.add(source)

  q = deque()
  q.append(source)

  prev = defaultdict(tuple)

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
  path.append(target)
  parent = prev[target]

  while parent:
    path.append(parent)
    parent = prev[parent]

  path.reverse()

  if path[0] == source:
    return path
  else:
    return []

def show_all(cave, units):
  for row in range(len(cave)):
    for col in range(len(cave[row])):

      unit_in_spot = False

      for unit in units:
        if unit.row == row and unit.col == col and unit.is_alive:
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
