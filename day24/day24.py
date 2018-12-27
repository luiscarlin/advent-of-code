import re
import copy
import math

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
    self.is_alive = True

  def attacked_with(self, damage):
    dead = int(damage/self.hit_points)

    if dead > self.num_units:
      dead = self.num_units
      self.num_units = 0
    else:
      self.num_units -= dead

    if (self.num_units == 0):
      self.is_alive = False

    return dead

  def get_effective_power(self):
    return self.num_units * self.attack_damage

  def __str__(self):
    return 'group_id={} group_type={} num_units={} hit_points={} attack_damage={} attack_type={} initiative={} weaknesses={} immunities={}'.format(
      self.group_id, self.group_type, self.num_units, self.hit_points, self.attack_damage, self.attack_type, self.initiative, self.weaknesses, self.immunities)

def get_groups(input_line, group_type):
  groups = []

  group_id = 1

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

def show_stats(groups):
  print('Immune System:')

  for group in [group for group in groups if group.group_type is IMMUNITY_TYPE and group.is_alive]:
    print('Group {} contains {} units'.format(group.group_id, group.num_units))

  print('Infection:')

  for group in [group for group in groups if group.group_type is INFECTION_TYPE and group.is_alive]:
    print('Group {} contains {} units'.format(group.group_id, group.num_units))

def calculate_damage(attacker, defender):
  damage = 0

  if attacker.attack_type in defender.weaknesses:
    damage = 2 * attacker.get_effective_power()
  elif attacker.attack_type in defender.immunities:
    damage = 0
  else:
    damage = attacker.get_effective_power()

  return damage

def attack(attacker, defender):
  damage = calculate_damage(attacker, defender)

  dead = defender.attacked_with(damage)

  attacker_group_type = 'Immune System' if attacker.group_type == IMMUNITY_TYPE else 'Infection'
  print('{} group {} attacks defending group {}, killing {} units'.format(attacker_group_type, attacker.group_id, defender.group_id, dead))

def defender_comparator(attacker, defender):
  damage = calculate_damage(attacker, defender)

  attacker_group_type = 'Immune System' if attacker.group_type == IMMUNITY_TYPE else 'Infection'
  print('{} group {} would deal defending group {} {} damage'.format(attacker_group_type, attacker.group_id, defender.group_id, damage))

  return (damage, defender.get_effective_power(), defender.initiative)

def battle(groups):
  show_stats(groups)

  copy_groups = copy.deepcopy(groups)

  copy_groups = [group for group in copy_groups if group.is_alive]
  sorted_cp_groups = sorted(copy_groups, key=lambda group: (group.get_effective_power(), group.initiative), reverse=True)

  chosen = set()
  pairs = []

  # find target
  print()
  for attacker in sorted_cp_groups:
    possible_targets = [group for group in sorted_cp_groups if group.group_type != attacker.group_type and group not in chosen]

    if possible_targets:
      target = max(possible_targets, key=lambda target: defender_comparator(attacker, target))

      chosen.add(target)

      pairs.append((attacker, target))

  # attack
  print()

  for pair in sorted(pairs, key=lambda pair: pair[0].initiative, reverse=True):
    attacker, target = pair

    if attacker.is_alive and target.is_alive:
      attack(attacker, target)

  return copy_groups

def main():
  _, immunity_lines, infection_lines = re.split('Immune System:|Infection:', open('./day24/input.txt').read())

  groups = get_groups(immunity_lines, IMMUNITY_TYPE)
  groups.extend(get_groups(infection_lines, INFECTION_TYPE))

  winning_army = 0

  while True:
    groups = battle(groups)

    immunity_groups_alive = [group for group in groups if group.group_type == IMMUNITY_TYPE and group.is_alive]
    infection_groups_alive = [group for group in groups if group.group_type == INFECTION_TYPE and group.is_alive]

    if len(infection_groups_alive) == 0:
      winning_army = immunity_groups_alive
      break

    if len(immunity_groups_alive) == 0:
      winning_army = infection_groups_alive
      break

  print('part 1', sum(group.num_units for group in winning_army))

if __name__ == '__main__':
  main()