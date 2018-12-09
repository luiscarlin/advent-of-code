#!/usr/bin/env python3

index = 0
input_list = list(map(int, open('input.txt').read().split()))

class Node:
  def __init__(self, num_children, num_metadata):
    self.num_children = num_children
    self.num_metadata = num_metadata
    self.metadata = []
    self.children = []

  def add_child(self, obj):
    self.children.append(obj)

  def add_metadata(self, int_metadata):
    self.metadata.append(int_metadata)

def get_next_int():
  global index
  global input_list
  index += 1

  return input_list[index - 1]

def construct_tree():
  number_children = get_next_int()
  number_metadata = get_next_int()

  node = Node(number_children, number_metadata)

  for _ in range(number_children):
    node.add_child(construct_tree())

  for _ in range(number_metadata):
    node.add_metadata(get_next_int())

  return node

def add_metadata(tree):
  total = 0

  total += sum(tree.metadata)

  for child in tree.children:
    total += add_metadata(child)

  return total

def get_value(tree):
  value = 0

  if len(tree.children) == 0:
    value = sum(tree.metadata)
  else:
    for entry in tree.metadata:
      if 0 < entry <= len(tree.children):
        value += get_value(tree.children[entry - 1])

  return value

def main():
  root = construct_tree()
  total = add_metadata(root)
  print('total sum metadata:', total)

  value = get_value(root)
  print('value is:', value)

if __name__ == '__main__':
  main()
