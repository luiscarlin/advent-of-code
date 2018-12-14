#!/usr/bin/env python3

import sys

UP = (-1, 0)
DOWN = (1, 0)
RIGHT = (0, 1)
LEFT = (0, -1)

class Cart:
  def __init__(self, row, col, direction):
    self.row = row
    self.col = col
    self.direction = direction
    self.number_intersections = 0

  def turn_for_intersection(self):
    factor = self.number_intersections % 3

    if factor == 0:
      # turn left
      if self.direction == UP:
        self.direction = LEFT
      elif self.direction == DOWN:
        self.direction = RIGHT
      elif self.direction == RIGHT:
        self.direction = UP
      elif self.direction == LEFT:
        self.direction = DOWN
    elif factor == 1:
      # continue straight
      pass
    elif factor == 2:
      # turn right
      if self.direction == UP:
        self.direction = RIGHT
      elif self.direction == DOWN:
        self.direction = LEFT
      elif self.direction == RIGHT:
        self.direction = DOWN
      elif self.direction == LEFT:
        self.direction = UP

    self.number_intersections += 1

  def __str__(self):
    if self.direction == UP:
      return '^'

    if self.direction == DOWN:
      return 'v'

    if self.direction == RIGHT:
      return '>'

    if self.direction == LEFT:
      return '<'

def main():
  carts, tracks = parse_input()

  # print('before')
  # for cart in carts:
  #   print(cart.row, cart.col)

  while True:
    if len(carts) == 1:
      print('location of the last cart left: {},{}'.format(carts[0].col, carts[0].row))
      sys.exit(0)

    carts.sort(key=lambda cart: (cart.row, cart.col))

    for cart in carts:
      next_row = cart.row + cart.direction[0]
      next_col = cart.col + cart.direction[1]

      if tracks[next_row][next_col] == '\\':
        if cart.direction == DOWN:
          cart.direction = RIGHT
        elif cart.direction == UP:
          cart.direction = LEFT
        elif cart.direction == RIGHT:
          cart.direction = DOWN
        elif cart.direction == LEFT:
          cart.direction = UP
      elif tracks[next_row][next_col] == '/':
        if cart.direction == DOWN:
          cart.direction = LEFT
        elif cart.direction == UP:
          cart.direction = RIGHT
        elif cart.direction == RIGHT:
          cart.direction = UP
        elif cart.direction == LEFT:
          cart.direction = DOWN
      elif tracks[next_row][next_col] == '+':
        cart.turn_for_intersection()

      for other in carts:
        if other.row == next_row and other.col == next_col:
          print('crash here: {},{}'.format(next_col, next_row))
          carts = [other for other in carts if (other.row, other.col) not in [(cart.row, cart.col),(next_row,next_col)]]

      cart.row = next_row
      cart.col = next_col

  for cart in carts:
    print(cart.row, cart.col)



def print_all(carts, tracks):
  for row in range(len(tracks)):
    for col in range(len(tracks[row])):

      cart_on_track = False
      for cart in carts:
        if cart.row == row and cart.col == col:
          cart_on_track = True
          print(cart, end = '')
          break

      if not cart_on_track:
        print(tracks[row][col], end = '')
    print()

def remove_carts_from_grid(grid):
  carts = []

  for row in range(len(grid)):
    for col in range(len(grid[row])):
      if (grid[row][col] == '^'):
        grid[row][col] = '|'
        carts.append(Cart(row, col, UP))
      elif (grid[row][col] == '>'):
        grid[row][col] = '-'
        carts.append(Cart(row, col, RIGHT))
      elif (grid[row][col] == 'v'):
        grid[row][col] = '|'
        carts.append(Cart(row, col, DOWN))
      elif (grid[row][col] == '<'):
        grid[row][col] = '-'
        carts.append(Cart(row, col, LEFT))
  return carts

def parse_input():
  carts = []
  track = []

  # for line in open('input.txt'):
  #   track.append(list(line.strip('/n')))

  for line in open('input.txt'):
    if line:
      track.append([c for c in line])

  # print(track)

  carts = remove_carts_from_grid(track)


  return carts, track

if __name__ == '__main__':
  main()