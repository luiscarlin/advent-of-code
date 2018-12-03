#!/usr/bin/env python3

import sys
import os

def main():
  filepath = sys.argv[1]

  if not os.path.isfile(filepath):
    print("File path {} does not exist. Exiting...".format(filepath))
    sys.exit()

  list_ids = process_file(filepath)

  repeated_twice = repeated_in_list(list_ids, 2)
  repeated_three_times = repeated_in_list(list_ids, 3)

  checksum = repeated_twice * repeated_three_times

  print('checksum:', checksum)

  similar = find_similar(list_ids)

  print('similar:', similar)

def find_similar(id_list):

  remainder = 0

  for id in id_list:
    id_list.remove(id)

    for other in id_list:
      diff_count = 0
      diff_index = 0

      for i in range(len(id)):
        if id[i] != other[i]:
          diff_count += 1
          diff_index = i

        if diff_count > 1:
          break

      if diff_count == 1:
        remainder = id[:diff_index] + id[diff_index + 1:]
        break

    if remainder != 0:
      break
  return remainder

def process_file(filepath):
  list_strings = []

  with open(filepath) as fp:
    for line in fp:
      line = line.strip()

      list_strings.append(line)

  return list_strings

def repeated(chars, num_repeated):
  count = dict.fromkeys(chars, 0)

  for char in chars:
    count[char] += 1

  return 1 if num_repeated in count.values() else 0

def repeated_in_list(list_of_ids, num_repeated):
  ids_with_repeated = 0
  for id in list_of_ids:
    ids_with_repeated += repeated(id, num_repeated)
  return ids_with_repeated

if __name__ == '__main__':
   main()
