#!/usr/bin/env python3

from collections import defaultdict
import re

'''
- Instruction pointer can be bound to a register so that it can be manipulated directly.
- setr/seti can function as absolute jumps
- addr/addi can function as relative jumps
- other opcodes will also trigger jumps
- #ip 1 - accesses to register 1 let the program indirectly access the instruction pointer itself
- 6 registers => [0, 0, 0, 0, 0, 0] => 5 not bound to the ip, behave as normal
- ip value is written to its register right before instruction is run
- value of register is written to the ip immediately after instruction is run
- add one to the ip to move to the next instruction (even if a prev instruction changed the ip)
- ip matches the position of the instruction starting at 0
- ip starts at 0
- if ip gets out of list of instructions, program halts
'''

def construct_fn(operation_func):
  def func(instruction, before_reg):
    regA, regB, regC = instruction

    result = operation_func(regA, regB, before_reg)

    after_reg = list(before_reg)
    after_reg[regC] = result

    return after_reg
  return func

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

def main():
  operations = construct_all_operations()

  lines = open('input.txt').read().strip().split('\n')

  ip_reg = int(lines[0].split()[1])
  program = lines[1:]

  registers = [1, 0, 0, 0, 0, 0]
  ip = 0

  num_loops = 0

  while ip < len(program):
    registers[ip_reg] = ip

    instruction = program[registers[ip_reg]].split()
    name = instruction[0]
    instruction = list(map(int, instruction[1:]))

    print('IN:', registers, end = '')
    print('    {} A={} B={} C={}'.format(name, instruction[0], instruction[1], instruction[2]), end = '')

    registers = operations[name](instruction, registers)

    print('    OUT:', registers)

    ip = registers[ip_reg] + 1

    # if num_loops == 500:
    #   break
    num_loops += 1

  print('part 1', registers[0])

if __name__ == '__main__':
  main()


