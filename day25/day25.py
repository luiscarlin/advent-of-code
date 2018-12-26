import networkx as nx

lines = open('./input.txt').read().split('\n')

points = []

for line in lines:
  x, y, z, w = map(int, line.split(','))
  points.append((x, y, z, w))

G = nx.Graph()

for (x1, y1, z1, w1) in points:
  for (x2, y2, z2, w2) in points:
    distance = abs(x1-x2) + abs(y1-y2) + abs(z1-z2) + abs(w1-w2)

    if distance <= 3:
      G.add_edge((x1, y1, z1, w1), (x2, y2, z2, w2))


print('part 1', nx.number_connected_components(G))