import re

points = {}

for line in open('./input.txt').read().split('\n'):
  x, y, z, radius = map(int, re.findall(r'-?\d+', line))
  points[(x, y, z)] = radius

strongest_point = max(points, key=lambda key: points[key])
strongest_radius = points[strongest_point]


points_in_range = 0

for point, value in points.items():
  x1, y1, z1 = strongest_point
  x2, y2, z2 = point

  distance = abs(x1-x2) + abs(y1-y2) + abs(z1-z2)

  if distance <= strongest_radius:
    points_in_range += 1

print('part 1', points_in_range)
