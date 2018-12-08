#!/usr/bin/env python3

from collections import defaultdict, deque

def main():
  parent_to_children, child_to_parents = get_relationships()

  print('parent_to_children', parent_to_children)
  print('children_to_parents', child_to_parents)

  roots = set(parent_to_children.keys()).difference(set(child_to_parents))
  roots_list = list(roots)

  first_node = min(roots_list)
  roots_list.remove(first_node)

  print('first_node', first_node)
  print('roots_list', roots_list)

  q = deque()
  q.append(first_node)

  available_vertices = roots_list

  print('queue', q)
  print('available_vertices', available_vertices)

  ordered_dag_list = []

  while True:
    current_vertex = q.popleft()
    print('current vertex', current_vertex)

    ordered_dag_list.append(current_vertex)
    print('orderedd_dag_list', ordered_dag_list)

    for child in parent_to_children[current_vertex]:
      child_to_parents[child].remove(current_vertex)

    print('new child to parent', child_to_parents)

    new_possible_vertices = parent_to_children[current_vertex]

    for poss in new_possible_vertices:
      if child_to_parents[poss] == []:
        available_vertices.append(poss)

    if len(available_vertices) == 0:
      print('done')
      break

    available_vertices = list(set(available_vertices))
    print('available vertices', available_vertices)

    next_vertex = min(available_vertices)
    available_vertices.remove(next_vertex)

    print('next vertex', next_vertex)
    print('available vertices', available_vertices)

    q.append(next_vertex)

  print('ordered dag', ''.join(ordered_dag_list))

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


def find_ends(dag):
  to_vertices = set([ v for l in dag.values() for v in l ])
  from_vertices = set(dag.keys())

  end = list(to_vertices.difference(from_vertices))
  head = list(from_vertices.difference(to_vertices))

  return head[0], end[0]

if __name__ == "__main__":
  main()