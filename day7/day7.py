#!/usr/bin/env python3

from collections import defaultdict, deque

def main():
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