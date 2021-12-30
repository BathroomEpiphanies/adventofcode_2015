import sys

def actual_program(a,b):
    if a==1:
        a *= 3
        a += 1
        a *= 3
        a += 1
        a += 1
        a *= 3
        a += 1
        a *= 3
        a += 1
        a += 1
        a *= 3
        a *= 3
        a += 1
        a += 1
        a *= 3
        a += 1
        a += 1
        a *= 3
        a += 1
        a += 1
        a *= 3
    else:
        a += 1
        a *= 3
        a += 1
        a *= 3
        a *= 3
        a *= 3
        a += 1
        a *= 3
        a += 1
        a *= 3
        a += 1
        a += 1
        a *= 3
        a *= 3
        a *= 3
        a += 1
    while a!=1:
        b += 1
        if a%2:
            a *= 3
            a += 1
        else:
            a //= 2
    return a,b


print('*1:',actual_program(0,0)[1])
print('*2:',actual_program(1,0)[1])
