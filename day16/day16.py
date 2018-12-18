#!/usr/bin/env python3

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
gtir => if valA > regB => 1 into


'''