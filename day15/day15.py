#!/usr/bin/env python3

class Unit:
  def __init__(self, row, col):
    self.row = row
    self.col = col
    self.attack_power = 3
    self.hit_points = 200

class Goblin(Unit):
  def __init__(self, row, col):
    Unit.__init__(self, row, col)

  def __str__(self):
    return 'G'

class Elf(Unit):
  def __init__(self, row, col):
    Unit.__init__(self, row, col)

  def __str__(self):
    return 'E'

def main():
  cave, units = parse_input()

  show_units(units)

  print('initial state')
  show_all(cave, units)

  for round in range(1, 4):
    print()

    # sort units

    # for unit in units:
      # find target


    print('end of round', round)
    show_all(cave, units)


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
      if cave[row][col] == 'G':
        units.append(Goblin(row, col))
        cave[row][col] = '.'
      elif cave[row][col] == 'E':
        units.append(Elf(row, col))
        cave[row][col] = '.'
  return cave, units

def show_units(units):
  for unit in units:
    print("{} at ({},{}) with attack power={} and hit points={}".format(unit, unit.row, unit.col, unit.attack_power, unit.hit_points))

if __name__ == '__main__':
  main()
