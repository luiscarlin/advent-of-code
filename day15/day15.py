#!/usr/bin/env python3

import sys
from collection import defaultdict

ELF_TYPE = 'E'
GOBLIN_TYPE = 'G'

class Unit:
  def __init__(self, row, col, unit_type):
    self.row = row
    self.col = col
    self.unit_type = unit_type
    self.attack_power = 3
    self.hit_points = 200

  def __str__(self):
    return self.unit_type

def main():
  cave, units = parse_input()

  print('initial state')
  show_all(cave, units)

  for round in range(1, 4):
    print()

    units = sorted(units, key = lambda unit: (unit.row, unit.col))

    for unit in units:
      target, distance, enemies_left = get_next_target(unit, units)

      if enemies_left == 0:
        print('No more targets left')
        sys.exit(0)

  #     if distance == 0:
  #       attack(unit, target)
  #     else:
  #       move(unit, target)

    print('end of round', round)
    show_all(cave, units)

def move(unit, target):
  print('moving')

def get_next_target(current, all):
  enemies_left = 0
  enemy = ''
  all_distances = defaultdict(int)

  for unit in all:
    if unit.unit_type != current.unit_type:
      enemies_left += 1

      distance = get_distance(current, unit):






  return enemy, distance, enemies_left

def attack(attacker, victim):
  print('attacking')

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
    print("{} at ({},{}) with attack power={} and hit points={}".format(unit, unit.row, unit.col, unit.attack_power, unit.hit_points))

if __name__ == '__main__':
  main()
