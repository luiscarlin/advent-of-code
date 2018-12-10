#!/usr/bin/env python3

import re
from collections import defaultdict

def process_file():
  coordinates = []
  change = []

  for line in open('input.txt'):
    x, y, dx, dy = map(int, re.findall(r'-?\d+', line))

    coordinates.append((x, y))
    change.append((dx, dy))

  return coordinates, change

def main():
  coordinates, change = process_file()

  min_area = get_area(coordinates)
  min_coordinates = []
  num_seconds = 0

  while True:
    move(coordinates, change)
    area = get_area(coordinates)

    if area > min_area:
      break

    if area < min_area:
      min_area = area
      min_coordinates = list(coordinates)

    num_seconds += 1

  print('hidden message:')
  pretty_print(min_coordinates)

  print('number of seconds:', num_seconds)

def find_corners(coordinates):
  min_x = min([ x for x, y in coordinates ])
  max_x = max([ x for x, y in coordinates ])
  min_y = min([ y for x, y in coordinates ])
  max_y = max([ y for x, y in coordinates ])

  return min_x, max_x, min_y, max_y

def get_area(coordinates):
  min_x, max_x, min_y, max_y = find_corners(coordinates)
  area = (max_x - min_x) * (max_y - min_y)

  return area

def pretty_print(coordinates):
  min_x, max_x, min_y, max_y = find_corners(coordinates)

  for y in range(min_y, max_y + 1):
    print()

    for x in range(min_x, max_x + 1):
      if (x, y) in coordinates:
        print('#', end = '')
      else:
        print('.', end = '')
  print('\n')

def move(coords, change):
  for pos in range(len(coords)):
    coords[pos] = (coords[pos][0] + change[pos][0], coords[pos][1] + change[pos][1])

if __name__ == '__main__':
  main()
