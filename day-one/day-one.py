#!/usr/bin/env python3

import sys
import os

def main():
  filepath = sys.argv[1]

  if not os.path.isfile(filepath):
    print("File path {} does not exist. Exiting...".format(filepath))
    sys.exit()

  total = 0

  with open(filepath) as fp:
    for line in fp:
      line = line.strip()

      operation = line[0]
      num = int(line[1:])

      if (operation is '+'):
        total += num

      if (operation is '-'):
        total -= num

  print("total:", total)

if __name__ == '__main__':
   main()