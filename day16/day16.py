#!/usr/bin/env python3

from collections import defaultdict
import re

'''
- registers = [0, 1, 2, 3]
- 16 opcodes
- instruction = opcode + input A + input B + output C (register)

addr => regA + regB => regC
addi => regA + valB => regC
mulr => regA * regB => regC
muli => regA * valB => regC
banr => regA & regB => regC
bani => regA & valB => regC
borr => regA | regB => regC
bori => regA | valB => regC
setr => regA => regC
seti => valA => regC
gtir => if valA > regB: 1 => regC else: 0 => regC
gtri => if regA > valB: 1 => regC else: 0 => regC
gtrr => if regA > regB: 1 => regC else: 0 => regC
eqir => if valA == regB: 1 => regC else: 0 => regC
eqri => if regA == valB: 1 => regC else: 0 => regC
eqrr => if regA == regB: 1 => regC else: 0 => regC
'''

# Before: [3, 2, 1, 1]
# 9 2 1 2
# After:  [3, 2, 2, 1]

def construct_fn(operation_func):
  def func(instruction, before_reg):
    opcode, regA, regB, regC = instruction

    result = operation_func(regA, regB, before_reg)

    after_reg = list(before_reg)
    after_reg[regC] = result

    return after_reg
  return func

def main():
  operations = construct_all_operations()

  lines = open('part1_input.txt').read().strip().split('\n')

  number_samples = 0

  possible_opcodes = defaultdict(set)

  for i, line in enumerate(lines):
    if 'Before' in line:
      before_reg = list(map(int, re.findall(r'-?\d+', line)))
      instruction = list(map(int, re.findall(r'-?\d+', lines[i + 1])))
      after_req = list(map(int, re.findall(r'-?\d+', lines[i + 2])))

      matching = 0
      for name, function in operations.items():
        if function(instruction, before_reg) == after_req:
          matching += 1
          possible_opcodes[name].add(instruction[0])

      if matching >= 3:
        number_samples += 1

  print('part 1', number_samples)

  opcodes = defaultdict(str)

  while possible_opcodes:
    for name, opcode_set in possible_opcodes.items():
      if len(opcode_set) == 1:
        opcode = list(opcode_set)[0]
        opcodes[opcode] = name

        del possible_opcodes[name]

        for v in possible_opcodes.values():
          if opcode in v:
            v.remove(opcode)

        break

  register = [0,0,0,0]

  for line in open('part2_input.txt'):
    instruction = list(map(int, re.findall(r'-?\d+', line)))
    register = operations[opcodes[instruction[0]]](instruction, register)

  print('part 2', register[0])

def construct_all_operations():
  operations = {
    'addr': construct_fn(lambda regA, regB, before_reg: before_reg[regA] + before_reg[regB]),
    'addi': construct_fn(lambda regA, regB, before_reg: before_reg[regA] + regB),
    'mulr': construct_fn(lambda regA, regB, before_reg: before_reg[regA] * before_reg[regB]),
    'muli': construct_fn(lambda regA, regB, before_reg: before_reg[regA] * regB),
    'banr': construct_fn(lambda regA, regB, before_reg: before_reg[regA] & before_reg[regB]),
    'bani': construct_fn(lambda regA, regB, before_reg: before_reg[regA] & regB),
    'borr': construct_fn(lambda regA, regB, before_reg: before_reg[regA] | before_reg[regB]),
    'bori': construct_fn(lambda regA, regB, before_reg: before_reg[regA] | regB),
    'setr': construct_fn(lambda regA, regB, before_reg: before_reg[regA]),
    'seti': construct_fn(lambda regA, regB, before_reg: regA),
    'gtir': construct_fn(lambda regA, regB, before_reg: 1 if regA > before_reg[regB] else 0),
    'gtri': construct_fn(lambda regA, regB, before_reg: 1 if before_reg[regA] > regB else 0),
    'gtrr': construct_fn(lambda regA, regB, before_reg: 1 if before_reg[regA] > before_reg[regB] else 0),
    'eqir': construct_fn(lambda regA, regB, before_reg: 1 if regA == before_reg[regB] else 0),
    'eqri': construct_fn(lambda regA, regB, before_reg: 1 if before_reg[regA] == regB else 0),
    'eqrr': construct_fn(lambda regA, regB, before_reg: 1 if before_reg[regA] == before_reg[regB] else 0),
  }
  return operations



if __name__ == '__main__':
  main()