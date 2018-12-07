#!/usr/bin/env python3

import collections

def main():
  coordinates = get_coordinates()

  max_x, max_y, min_x, min_y = find_corners(coordinates)

  edge_areas = []

  for x in range(min_x, max_x):
    for y in range(min_y, max_y):
      distances = collections.defaultdict(int)
      for coordinate in coordinates.keys():
        distance = calculate_distance((x, y), coordinate)
        distances[coordinate] = distance

      minimum_distance = min(distances.values())

      indices = [i for i, x in enumerate(distances.values()) if x == minimum_distance]

      if len(indices) == 1:
        coord_with_least_distance = min(distances, key=distances.get)
        coordinates[coord_with_least_distance] += 1
        if (x == min_x or x == max_x or y == min_y or y == max_y):
          edge_areas.append(coord_with_least_distance)


  for to_delete in set(edge_areas):
    del coordinates[to_delete]

  biggest_area = max(coordinates, key=coordinates.get)
  print('biggest area around', biggest_area)
  print('with locations =', coordinates[biggest_area])

def get_coordinates():
  coordinates = collections.defaultdict(int)
  lines = open('./input.txt').readlines()

  for line in lines:
    x, y = line.split(',')
    x, y = int(x), int(y)
    coordinates[x, y] = 0

  return coordinates

def find_corners(coordinates):
  max_x, max_y = list(coordinates.keys())[0]
  min_x, min_y = list(coordinates.keys())[0]

  for x, y in coordinates.keys():
    if x > max_x:
      max_x = x
    if y > max_y:
      max_y = y
    if x < min_x:
      min_x = x
    if y < min_y:
      min_y = y

  return max_x, max_y, min_x, min_y

def calculate_distance(point1, point2):
  return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

if __name__ == '__main__':
  main()