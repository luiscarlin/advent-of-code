#!/usr/bin/env python3

from collections import defaultdict, deque

def main():
  part1()
  part2()

def get_step_time(letter):
  return ord(letter) - 4

def do_work(current):
  work_done = []

  for k in current:
    current[k] = current[k] - 1

    if current[k] == 0:
      work_done.append(k)

  for done in work_done:
    del current[done]

  return current, work_done

def has_prereqs(vertex, prereqs):
  return not prereqs[vertex] == []

def assign_work(number_workers, current_work, available_vertices, prerequisites):
  available_vertices = sorted(list(set(available_vertices)))

  if (len(current_work)) == number_workers:
    return current_work, available_vertices

  for possible_step in list(available_vertices):
    if has_prereqs(possible_step, prerequisites):
      continue

    if len(current_work) < number_workers:
      current_work[possible_step] = get_step_time(possible_step)
      available_vertices.remove(possible_step)

  return current_work, available_vertices

def remove_prereq(done_step, child_to_parents, parent_to_children):
  for child in parent_to_children[done_step]:
    child_to_parents[child].remove(done_step)

  return child_to_parents, parent_to_children


def part2():
  parent_to_children, child_to_parents = get_relationships()

  roots = set(parent_to_children.keys()).difference(set(child_to_parents))
  roots_list = list(roots)

  current_work = defaultdict(int)
  number_workers = 5
  time = 0
  available_vertices = roots_list

  current_work, available_vertices = assign_work(number_workers, current_work, available_vertices, child_to_parents)

  while len(current_work) > 0:
    time += 1

    current_work, work_done = do_work(current_work)

    for done_step in work_done:
      child_to_parents, parent_to_children = remove_prereq(done_step, child_to_parents, parent_to_children)

      new_possible_vertices = parent_to_children[done_step]
      available_vertices.extend(new_possible_vertices)

    if len(available_vertices) > 0:
      current_work, available_vertices = assign_work(number_workers, current_work, available_vertices, child_to_parents)

  print('time:', time)


def part1():
  parent_to_children, child_to_parents = get_relationships()

  roots = set(parent_to_children.keys()).difference(set(child_to_parents))
  roots_list = list(roots)

  first_node = min(roots_list)
  roots_list.remove(first_node)

  q = deque()
  q.append(first_node)

  available_vertices = roots_list

  ordered_dag_list = []

  while True:
    current_vertex = q.popleft()
    ordered_dag_list.append(current_vertex)

    for child in parent_to_children[current_vertex]:
      child_to_parents[child].remove(current_vertex)

    new_possible_vertices = parent_to_children[current_vertex]

    for poss in new_possible_vertices:
      if child_to_parents[poss] == []:
        available_vertices.append(poss)

    if len(available_vertices) == 0:
      break

    available_vertices = list(set(available_vertices))

    next_vertex = min(available_vertices)
    available_vertices.remove(next_vertex)

    q.append(next_vertex)

  print('ordered dag:', ''.join(ordered_dag_list))

def get_relationships():
  parent_to_children = defaultdict(list)
  child_to_parents = defaultdict(list)

  for line in open('./input.txt').readlines():
    words = line.split()
    v1 = words[1]
    v2 = words[7]

    parent_to_children[v1].append(v2)
    child_to_parents[v2].append(v1)

  return parent_to_children, child_to_parents

if __name__ == "__main__":
  main()