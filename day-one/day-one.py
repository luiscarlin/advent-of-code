#!/usr/bin/env python3

# ./day-one.py ./input.txt

import sys
import os

def main():
  filepath = sys.argv[1]

  if not os.path.isfile(filepath):
    print("File path {} does not exist. Exiting...".format(filepath))
    sys.exit()

  frequencies = []
  accumulator = 0

  (total, first_repeated_freq) = process_file(accumulator, filepath, frequencies)
  print("total:", total)

  while(first_repeated_freq is 'NONE'):
    (total, first_repeated_freq) = process_file(total, filepath, frequencies)

  print("first repeated:", first_repeated_freq)

def calculate(op, num, acc):
  if (op is '+'):
    acc += num

  if (op is '-'):
    acc -= num

  return acc

def process_file(accumulator, filepath, frequencies):
  if (accumulator is 0):
    frequencies.append(accumulator)

  first_repeated_freq = 'NONE'

  with open(filepath) as fp:
    for line in fp:
      line = line.strip()

      operation = line[0]
      num = int(line[1:])

      accumulator = calculate(operation, num, accumulator)

      if (accumulator in frequencies and first_repeated_freq is 'NONE'):
        first_repeated_freq = accumulator

      frequencies.append(accumulator)

  return (accumulator, first_repeated_freq)

if __name__ == '__main__':
   main()
