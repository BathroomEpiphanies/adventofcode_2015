import json
import re
import sys

from collections import namedtuple
from functools import cache


# match 'a op b -> c'
r = r'(?P<a>[0-9a-z]+)? *(?P<op>AND|OR|NOT|LSHIFT|RSHIFT)? *(?P<b>[0-9a-z]+)? *-> *(?P<c>[a-z]+)'
Connection = namedtuple('Connection',['a','op','b'])
circuit = {m['c']:Connection(m['a'],m['op'],m['b']) for l in sys.stdin.readlines() for m in [re.match(r,l).groupdict()]}

#print(json.dumps(circuit,indent=4,sort_keys=True))


def calculate(circuit, wire):
    @cache
    def foo(wire):
        try:
            return(int(wire))
        except ValueError:
            pass
        
        conn = circuit[wire]
        if not conn.op:
            return foo(conn.a)
        elif conn.op == 'AND':
            return foo(conn.a) & foo(conn.b)
        elif conn.op == 'OR':
            return foo(conn.a) | foo(conn.b)
        elif conn.op == 'NOT':
            return ((1<<16)-1) & ~foo(conn.b)
        elif conn.op == 'LSHIFT':
            return foo(conn.a) << foo(conn.b)
        elif conn.op == 'RSHIFT':
            return foo(conn.a) >> foo(conn.b)
    return foo(wire)


for k in sorted(circuit.keys()):
    print(f'{k}: {calculate(circuit,k)}', file=sys.stderr)

val = calculate(circuit,'a')
print(f'*1: {val}')

circuit['b'] = Connection(val,None,None)
val = calculate(circuit,'a')
print(f'*2: {val}')
