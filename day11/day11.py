#!/usr/bin/env python3

from collections import defaultdict

power_grid = defaultdict(int)
partial_sums = defaultdict(int)

def main():
  populate_power_grid()
  populate_partial_sums()
  part1()
  part2()

def populate_power_grid():
  global power_grid
  serial_number = 9005
  # serial_number = 18

  for y in range(1, 301):
    for x in range(1, 301):
      power_grid[(x, y)] = get_power_level(x, y, serial_number)

def get_partial_sum(x, y):
  if x < 1 or y < 1:
    return 0
  return partial_sums[(x, y)]

def populate_partial_sums():
  global partial_sums

  for y in range(1, 301):
    for x in range(1, 301):
      partial_sums[(x, y)] = power_grid[(x, y)] + get_partial_sum(x - 1, y) + get_partial_sum(x, y - 1) - get_partial_sum(x - 1, y - 1)

def get_power_in_area(x, y, width):
  return get_partial_sum(x, y) + get_partial_sum(x - width, y - width) - get_partial_sum(x - width, y) - get_partial_sum(x, y - width)

def part2():
  max_power = 0
  top_left = (0, 0)
  max_size = 0

  for y in range(1, 301):
    for x in range(1, 301):
      for size in range(1, 301):
        power = get_power_in_area(x, y, size)

        if max_power < power:
          max_power = power
          top_left = (x - size + 1, y - size + 1)
          max_size = size

  print('part2')
  print('max power', max_power)
  print('answer', top_left, max_size)

def part1():
  size = 3
  max_power = 0
  top_left = (0, 0)

  for x,y in power_grid.keys():
    coords = get_window(x, y, size)

    out_of_power_grid = False

    for coord in coords:
      if coord[0] > 300 or coord[1] > 300:
        out_of_power_grid = True
        break

    if out_of_power_grid:
      continue

    total_power = 0
    for coord in coords:
      total_power += power_grid[coord]

    if total_power > max_power:
      max_power = total_power
      top_left = (x, y)

  print('part1')
  print('max power', max_power)
  print('top left', top_left)


def get_window(x, y, size):
  coordinates = []

  for dy in range(0, size):
    for dx in range(0, size):
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
