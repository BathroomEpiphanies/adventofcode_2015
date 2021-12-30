import sys
import re
from collections import namedtuple

Instruction = namedtuple('instruction',['op','reg','val'])

program = []
for line in (l.strip() for l in sys.stdin.readlines()):
    op,line = line[:3],line[4:]
    if op in ['jie','jio']:
        reg,line = line.split(', ')
    elif op not in ['jmp']:
        reg,line = line[0],line[1:]
    else:
        reg = None
    if line:
        val = int(line)
    else:
        val = None
    program.append(Instruction(op,reg,val))
for p in program:
    print(p)


memory = {'a':1,'b':0}

pointer = 0
while pointer<len(program):
    instr = program[pointer]
    print(pointer,instr,memory)
    if instr.op == 'hlf':
        memory[instr.reg] //= 2
        pointer += 1
    elif instr.op == 'tpl':
        memory[instr.reg] *= 3
        pointer +=1
    elif instr.op == 'inc':
        memory[instr.reg] += 1
        pointer += 1
    elif instr.op == 'jmp':
        pointer += instr.val
    elif instr.op == 'jie':
        if memory[instr.reg]%2:
            pointer += instr.val
        else:
            pointer += 1
    elif instr.op == 'jio':
        if memory[instr.reg] == 1:
            pointer += instr.val
        else:
            pointer += 1

print(memory)
