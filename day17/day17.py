from collections import namedtuple

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

X_DIR = [0, 1, 0, -1]
Y_DIR = [-1, 0, 1, 0]

WATER_SOURCE = (500, 0)

def get_point(dir, from_point):
  return (from_point[0] + X_DIR[dir], from_point[1] + Y_DIR[dir])

def print_map(clay, flowing, still, x1=300, x2=700, y1=0, y2=1000):
  def char(p):
    if p == WATER_SOURCE:
      return '+'
    elif p in clay:
      return '#'
    elif p in both:
      return '$'
    elif p in still:
      return '~'
    elif p in flowing:
      return '|'
    else:
      return '.'

  both = flowing & still
  print('\n'.join(''.join(char((x, y)) for x in range(x1, x2 + 1)) for y in range(y1, y2 + 1)))

def get_clay():
  clay = set()

  for line in open('./day17/input.txt').read().split('\n'):
    row = []
    col = []

    parts = line.strip().split(',')

    for part in parts:
      part = part.replace(' ', '')
      if 'x' in part:
        part = part.replace('x=', '')

        if '..' in part:
          start, finish = list(map(int, part.split('..')))

          for i in range(start, finish + 1):
            col.append(i)
        else:
          col.append(int(part))

      if 'y' in part:
        part = part.replace('y=', '')

        if '..' in part:
          start, finish = list(map(int, part.split('..')))

          for i in range(start, finish + 1):
            row.append(i)
        else:
          row.append(int(part))

    col = list(map(int, col))
    row = list(map(int, row))

    if len(col) == 1:
      for r in row:
        clay.add((col[0], r ))
    else:
      for c in col:
        clay.add((c, row[0]))

  return clay

def simulate():
  clay = get_clay()

  lowest_y, highest_y = max(p[1] for p in clay), min(p[1] for p in clay)
  flowing, still, to_fall, to_spread = set(), set(), set(), set()

  to_fall.add(WATER_SOURCE)

  while to_fall or to_spread:
    while to_fall:
      tf = to_fall.pop()
      res = fall(tf, lowest_y, clay, flowing)
      if res:
        to_spread.add(res)

    while to_spread:
      ts = to_spread.pop()
      rl, rr = spread(ts, clay, flowing, still)
      if not rr and not rl:
        to_spread.add(get_point(UP, ts))
      else:
        if rl:
          to_fall.add(rl)
        if rr:
          to_fall.add(rr)

  # print_map(clay, flowing, still, y2=lowest_y)
  total_water = len([p for p in (flowing | still) if p[1] >= highest_y])
  still_water = len([p for p in still if p[1] >= highest_y])

  print('Part 1 => Total Water = {}'.format(total_water))
  print('Part 2 => Still Water = {}'.format(still_water))

def fall(pos, ly, clay, flowing):
  while pos[1] < ly:
    posd = get_point(DOWN, pos)
    if posd not in clay:
      flowing.add(posd)
      pos = posd
    elif posd in clay:
      return pos
  return None

def spread(pos, clay, flowing, still):
  temp = set()
  pl = spread_r(pos, LEFT, clay, still, temp)
  pr = spread_r(pos, RIGHT, clay, still, temp)
  if not pl and not pr:
    still.update(temp)
  else:
    flowing.update(temp)
  return pl, pr

def spread_r(pos, off, clay, still, temp):
  pos1 = pos
  while pos1 not in clay:
    temp.add(pos1)
    pos2 = get_point(DOWN, pos1)
    if pos2 not in clay and pos2 not in still:
      return pos1
    pos1 = get_point(off, pos1)
  return None

if __name__ == '__main__':
  simulate()
