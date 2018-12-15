#!/usr/bin/env python3

def part2():
  print('\npart2\n----\n')

  pattern = '824501'
  recipes = '37'

  elf1_index = 0
  elf2_index = 1

  while pattern not in recipes[-7:]:
    recipes += str(int(recipes[elf1_index]) + int(recipes[elf2_index]))

    elf1_index = (int(recipes[elf1_index]) + 1 + elf1_index) % len(recipes)
    elf2_index = (int(recipes[elf2_index]) + 1 + elf2_index) % len(recipes)

  print('# recipes left of the pattern:', recipes.index(pattern))

def part1():
  print('\npart1\n----\n')

  start = '824501'
  recipes = '37'

  elf1_index = 0
  elf2_index = 1

  while len(recipes) != int(start) + 10:
    sum = int(recipes[elf1_index]) + int(recipes[elf2_index])

    recipes += str(sum)

    elf1_index = (int(recipes[elf1_index]) + 1 + elf1_index) % len(recipes)
    elf2_index = (int(recipes[elf2_index]) + 1 + elf2_index) % len(recipes)

  print('Last 10:', recipes[-10:])

def main():
  part1()
  part2()

if __name__ == '__main__':
  main()
