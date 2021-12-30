import sys


#lines = [l.strip()[1:-1] for l in sys.stdin.readlines()]
lines = [l.strip() for l in sys.stdin.readlines()]
#print(lines)

string_total = 0
code_total = 0
for l in lines:
    decoded = l[1:-1].encode().decode('unicode-escape')
    #print(f'] {decoded} [ {len(decoded)}')
    code_total += len(l)
    string_total += len(decoded)

print(f'{code_total} - {string_total} = {code_total-string_total}', file=sys.stderr)
print(f'*1: {code_total-string_total}')


string_total = 0
code_total = 0
for l in lines:
    encoded = '"'+l.encode('unicode-escape').decode().replace('"','\\"')+'"'
    #print(f'] {encoded} [ {len(encoded)}')
    string_total += len(l)
    code_total += len(encoded)

print(f'{code_total} - {string_total} = {code_total-string_total}', file=sys.stderr)
print(f'*2: {code_total-string_total}')
