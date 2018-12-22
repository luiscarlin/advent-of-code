#!/usr/bin/env python3

'''
- figure out how the program works and cause it to halt.
- You can only control register 0; every other register begins at 0 as usual.
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

  registers = [100, 0, 0, 0, 0, 0]
  ip = 0

  loops =0

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

    # loops += 1
    # if loops == 50:
    #   break

if  __name__ == '__main__':
  main()
