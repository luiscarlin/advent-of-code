#!/usr/bin/env python3


def part2():
  print('part2')

  pattern = '824501'

  recipes = [3, 7]

  # 51589167792510710
  # 5158916779

  elf1_index = 0
  elf2_index = 1

  while True:
    recipes_str_list = list(map(str, recipes))
    recipes_str = ''.join(recipes_str_list)

    if pattern in recipes_str:
       print('pattern found')
       break

    sum = recipes[elf1_index] + recipes[elf2_index]

    sum_list = list(map(int, list(str(sum))))

    recipes.extend(sum_list)

    elf1_index = ((recipes[elf1_index] + 1) + elf1_index) % len(recipes)
    elf2_index = ((recipes[elf2_index] + 1) + elf2_index) % len(recipes)

def part1():
  print('part1')
  # record_after = 9
  record_after = 824501

  recipes = [3, 7]

  # 51589167792510710
  # 5158916779

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

  # print('recipes:', recipes)

  recipes_str_list = list(map(str, recipes[record_after:]))

  last_10 = ''.join(recipes_str_list)

  print('last 10:', last_10)

def main():
  # part1()
  part2()

if __name__ == '__main__':
  main()