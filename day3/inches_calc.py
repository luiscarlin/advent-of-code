#!/usr/bin/env python3

import collections

def main():
  coordinates = collections.defaultdict(int)

  lines = open('input.txt').readlines()

  for line in lines:
    id, x, y, width, height = parse_claim(line)

    for dx in range(width):
      for dy in range(height):
        coordinates[x + dx, y + dy] += 1

  shared = 0

  for (x,y), val in coordinates.items():
    if val > 1:
      shared += 1

  print ('shared overlaps', shared)

  for line in lines:
    id, x, y, width, height = parse_claim(line)

    no_overlaps = True

    for dx in range(width):
      for dy in range(height):
        if coordinates[x + dx, y + dy] > 1:
          no_overlaps = False

    if no_overlaps:
      print ('claim with no overlaps', id)


def parse_claim(claim):
  claim = claim.split()
  id = claim[0]
  x, y = claim[2].split(',')
  x, y = int(x), int(y[:-1])
  width, height = claim[3].split('x')
  width, height = int(width), int(height)

  return id, x, y, width, height

if __name__ == '__main__':
   main()
