#!/usr/bin/env python3


def main():
  string = open('input.txt').read()

  reduced = react(string)

  print('star 1', reduced)


def react(polymer):
  processed = False

  while (not processed):
    for index, char in enumerate(polymer):
      next_index = index + 1

      if len(polymer) == next_index:
        processed = True
        break

      next_char = polymer[next_index]

      if char.lower() == next_char.lower():
        if char.islower() and next_char.isupper() or char.isupper() and next_char.islower():
          polymer = polymer[:index] + polymer[next_index + 1:]
          break

  return polymer


if __name__ == '__main__':
   main()
