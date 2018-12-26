import re
import copy

IMMUNITY_TYPE = 0
INFECTION_TYPE = 1

class Group:
  def __init__(self, group_id, group_type, num_units, hit_points, attack_damage, attack_type, initiative, weaknesses, immunities):
    self.group_id = group_id
    self.group_type = group_type
    self.num_units = num_units
    self.hit_points = hit_points
    self.attack_damage = attack_damage
    self.attack_type = attack_type
    self.initiative = initiative
    self.weaknesses = weaknesses
    self.immunities = immunities

  def get_effective_power(self):
    return self.num_units * self.attack_damage

  def is_dead(self):
    return self.num_units == 0

  def __str__(self):
    return 'group_id={} group_type={} num_units={} hit_points={} attack_damage={} attack_type={} initiative={} weaknesses={} immunities={}'.format(
      self.group_id, self.group_type, self.num_units, self.hit_points, self.attack_damage, self.attack_type, self.initiative, self.weaknesses, self.immunities)

def get_groups(input_line, group_type):
  groups = []

  group_id = 0

  for line in input_line.split('\n'):
    if line:
      weaknesses = []
      immunities = []

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

      num_units = int(words[0])
      hit_points = int(words[4])
      attack_damage = int(words[12])
      attack_type =  words[13]
      initiative = int(words[17])

      groups.append(Group(group_id, group_type, num_units, hit_points, attack_damage, attack_type, initiative, weaknesses, immunities))

      group_id += 1

  return groups

_, immunity_lines, infection_lines = re.split('Immune System:|Infection:', open('./day24/input.txt').read())

groups = get_groups(immunity_lines, IMMUNITY_TYPE)
groups.extend(get_groups(infection_lines, INFECTION_TYPE))

for group in groups:
  copy_groups = copy.deepcopy(groups)

  attacker = sorted(groups, key=lambda group: (group.get_effective_power(), group.initiative), reverse=True)[0]
