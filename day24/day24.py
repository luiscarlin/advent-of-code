import re

class Unit:
  def __init__(self, hit_points, attack_damage, attack_type, initiative, weaknesses, immunities):
    self.hit_points = hit_points
    self.attack_damage = attack_damage
    self.attack_type = attack_type
    self.initiative = initiative
    self.weaknesses = weaknesses
    self.immunities = immunities

# 18 units each with 729 hit points (weak to fire; immune to cold, slashing) with an attack that does 8 radiation damage at initiative 10
def get_units(input_line):
  for line in input_line.split('\n'):

    weaknesses = []
    immunities = []

    if line:
      if '(' in line:
        weak_and_immunities = line.split('(')[1].split(')')[0].split(';')

        for item in weak_and_immunities:
          if 'weak' in item:
            weaknesses = item.strip().split('weak to')[1].replace(' ', '').split(',')

          if 'immune' in item:
            immunities = item.strip().split('immune to')[1].replace(' ', '').split(',')

        line = re.sub(r'\(.*\) ', '', line)

      words = line.split()
      assert(len(words) == 18)











  return []

_, immunity_lines, infection_lines = re.split('Immune System:|Infection:', open('./input.txt').read())

immunity_units = get_units(immunity_lines)
# infection_units = get_units(infection_lines)


