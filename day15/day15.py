#!/usr/bin/env python3

class Unit:
  def __init__(self, row, col):
    self.row = row
    self.col = col

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
  cave, goblins, elves = parse_input()
  show_all(cave, goblins, elves)

def show_all(cave, goblins, elves):
  for row in range(len(cave)):
    for col in range(len(cave[row])):

      unit_in_spot = False

      for goblin in goblins:
        if goblin.row == row and goblin.col == col:
          print(goblin, end = '')
          unit_in_spot = True
          break

      if not unit_in_spot:
        for elf in elves:
          if elf.row == row and elf.col == col:
            print(elf, end = '')
            unit_in_spot = True
            break

      if not unit_in_spot:
        print(cave[row][col], end = '')
    print()

def parse_input():
  cave = []
  goblins = []
  elves = []

  for line in open('input.txt'):
    cave.append([c for c in line.strip()])

  for row in range(len(cave)):
    for col in range(len(cave[row])):
      if cave[row][col] == 'G':
        goblins.append(Goblin(row, col))
        cave[row][col] = '.'
      elif cave[row][col] == 'E':
        elves.append(Elf(row, col))
        cave[row][col] = '.'
  return cave, goblins, elves

if __name__ == '__main__':
  main()
