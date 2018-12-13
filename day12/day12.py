#!/usr/bin/env python3

def get_total(current_state, offset):
  total = 0

  for i in range(len(current_state)):
    pot = i - 5 - offset

    if current_state[i] == '#':
      total += pot
  return total


def main():
  lines = open('input.txt').readlines()

  initial_state = lines[0].split(': ')[1].strip()

  tranformations = {}

  for line in lines[2:]:
    left, right = line.split(' => ')
    tranformations[left.strip()] = right.strip()

  current_state = '.....' + initial_state + '.....'

  prev_total = 0
  offset = 0

  for generations in range(1, 500):
    next_state = current_state

    for i in range(len(current_state)):
      center = i + 2
      pattern = current_state[i: i + 5]

      if (pattern in tranformations):
        next_state = next_state[:center] + tranformations[pattern] + next_state[center + 1:]

    current_state = '.....' + next_state + '.....'
    offset += 5

    total = get_total(current_state, offset)
    print('generation: ', generations, 'total:', total, 'different:', total - prev_total)

    prev_total = total


if __name__ == '__main__':
  main()