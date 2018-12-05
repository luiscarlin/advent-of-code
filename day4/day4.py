#!/usr/bin/env python3

import collections

id_by_minute = collections.defaultdict(int)
mins_asleep = collections.defaultdict(int)

lines = open('input.txt').readlines()

lines.sort()

id = 0
start = 0
end = 0

for line in lines:
  words = line.split()

  if "Guard" in line:
    id = words[3]
    id = id[1:]
    continue

  minute = int(words[1].split(":")[1][:-1])

  if "falls asleep" in line:
    start = minute
    continue

  if "wakes up" in line:
    end = minute

    for time in range(start, end):
      id_by_minute[(id, time)] += 1
      mins_asleep[id] += 1

id_most_sleeping = max(mins_asleep, key=mins_asleep.get)

filtered_id_by_minute = {k:v for (k,v) in id_by_minute.items() if id_most_sleeping in k}

most_popular_min = max(filtered_id_by_minute, key=filtered_id_by_minute.get)

print('product 1', int(most_popular_min[0]) * most_popular_min[1])

data_max_min_to_sleep = max(id_by_minute, key=id_by_minute.get)
print('product 2', int(data_max_min_to_sleep[0]) * data_max_min_to_sleep[1])
