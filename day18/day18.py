#!/usr/bin/env python3

import copy

'''
The lumber collection area is 50 acres by 50 acres
each acre can be either open ground (.), trees (|), or a lumberyard (#).

one minute, an open acre can fill with trees, a wooded acre can be converted to a lumberyard, or a lumberyard can be cleared to open ground (the lumber having been sent to other projects).

'''

TREE = '|'
LUMBER = '#'
OPEN = '.'

def show_all(data):
  for row in range(len(data)):
    for col in range(len(data[row])):
      print(data[row][col], end='')
    print()

def calculate_answer(data):
  final_num_trees = sum([unit.count(TREE) for unit in data])
  final_num_lumber = sum([unit.count(LUMBER) for unit in data])

  return final_num_lumber * final_num_trees

def get_neighbors_nums(row, col, data):
  directions = [(1, 0), (1, 1), (0, 1), (-1, 0), (-1, -1), (0, -1), (1, -1), (-1, 1)]

  num_trees = 0
  num_open_acre = 0
  num_lumber = 0

  for dir in directions:
    r = row + dir[0]
    c = col + dir[1]

    if r < 0 or c < 0 or r >= len(data) or c >= len(data):
      continue

    unit = data[r][c]

    if unit == TREE:
      num_trees += 1
    elif unit == LUMBER:
      num_lumber += 1
    elif unit == OPEN:
      num_open_acre += 1

  return num_trees, num_open_acre, num_lumber

data = []

for line in open('./input.txt'):
  if line:
    data.append(list(line.strip('\n')))

minute = 0

# show_all(data)

prev_total = 0

while minute < 1000:
  next_data = copy.deepcopy(data)

  for row in range(len(data)):
    for col in range(len(data[row])):

      unit = data[row][col]

      num_trees, num_open_acre, num_lumber = get_neighbors_nums(row, col, data)

      if unit == OPEN:
        if num_trees >= 3:
          next_data[row][col] = TREE
      elif unit == TREE:
        if num_lumber >= 3:
          next_data[row][col] = LUMBER
      elif unit == LUMBER:
        if num_lumber >= 1 and num_trees >= 1:
          next_data[row][col] = LUMBER
        else:
          next_data[row][col] = OPEN

  data = next_data
  minute += 1
  new_total = calculate_answer(data)
  print('after minute={}, total={}, diff={}'.format(minute, new_total, new_total - prev_total))
  prev_total = new_total
  # show_all(data)
