#!/usr/bin/env python3

from collections import defaultdict

def main():
  serial_number = 9005

  grid = defaultdict(int)

  for y in range(1, 301):
    for x in range(1, 301):
      grid[(x, y)] = get_power_level(x, y, serial_number)

  max_power = 0
  top_left = (0, 0)

  for x,y in grid.keys():
    if x > 298 or y > 298:
      continue

    coords = get_window(x, y)

    total_power = 0
    for coord in coords:
      total_power += grid[coord]

    if total_power > max_power:
      max_power = total_power
      top_left = (x, y)

  print('max power', max_power)
  print('top left', top_left)


def get_window(x, y):
  coordinates = []

  for dy in range(0, 3):
    for dx in range(0, 3):
      coordinates.append((x + dx, y + dy))

  return coordinates

def get_power_level(x, y , serial_number):
  rack_id = x + 10
  result = ((rack_id * y) + serial_number) * rack_id

  hundreds_digit = 0

  if len(str(result)) >= 3:
    hundreds_digit = int(str(result)[-3])

  power_level = hundreds_digit - 5

  return power_level

if __name__ == '__main__':
  main()
