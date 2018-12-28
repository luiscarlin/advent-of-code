'''
x = col
y = row
'''

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

COL_DIR = [0, 1, 0, -1]
ROW_DIR = [-1, 0, 1, 0]

def get_clay():
  # (col, row)
  clay = []

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
        clay.append((col[0], r ))
    else:
      for c in col:
        clay.append((c, row[0]))

  return clay

def print_map(water_source,  clay, water_flow):
  cols = [entry[0] for entry in clay]
  cols.append(water_source[0])

  min_col, max_col = min(cols), max(cols)

  rows = [entry[1] for entry in clay]
  rows.append(water_source[1])

  min_row, max_row = min(rows), max(rows)

  for row in range(min_row, max_row + 1):
    for col in range(min_col, max_col + 1):
      point = (col, row)

      char_to_print = '.'

      if point in clay:
        char_to_print = '#'
      elif point == water_source:
        char_to_print = '+'
      elif point in water_flow:
        char_to_print = '|'

      print(char_to_print, end='')

    print()

def simulate(water_source, clay):

  water_flow = []

  print('\nINITIALLY')
  print_map(water_source, clay, water_flow)

  for time in range(1, 10):
    flow(water_source, water_flow, clay)

    print('\nAFTER TIME', time)
    print_map(water_source, clay, water_flow)

def flow(water_source, water_flow, clay):
  if len(water_flow) is 0:
    water_flow.append(get_point(DOWN, water_source))
    return

  for flow in water_flow:
    point_down = get_point(DOWN, flow)

    if point_down not in water_flow and point_down not in clay:
      water_flow.append(point_down)
      return

def main():
  clay = get_clay()

  water_source = (500, 0)

  simulate(water_source, clay)

def get_point(dir, from_point):
  return (from_point[0] + COL_DIR[dir], from_point[1] + ROW_DIR[dir])

if __name__ == '__main__':
  main()
