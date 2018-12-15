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

  record_after = 824501

  recipes = [3, 7]

  elf1_index = 0
  elf2_index = 1

  while True:
    if len(recipes) == record_after + 10:
      break

    sum = recipes[elf1_index] + recipes[elf2_index]

    sum_list = list(map(int, list(str(sum))))

    recipes.extend(sum_list)

    elf1_index = ((recipes[elf1_index] + 1) + elf1_index) % len(recipes)
    elf2_index = ((recipes[elf2_index] + 1) + elf2_index) % len(recipes)

  recipes_str_list = list(map(str, recipes[record_after:]))

  last_10 = ''.join(recipes_str_list)

  print('Last 10:', last_10)

def main():
  part1()
  part2()

if __name__ == '__main__':
  main()