import sys

from itertools import product
from more_itertools import pairwise

class Password:
    incrementer = {
        a:b for a,b in zip(
            'abcdefghijklmnopqrstuvwxyz',
            'bcdefghjjkmmnppqrstuvwxyza'
        )
    }
                                      
    def __init__(self,word):
        array = list(word)
        illegal = False
        for i,d in enumerate(array):
            if illegal:
                array[i] = 'a'
            elif d in 'ilo':
                array[i] = Password.incrementer[d]
                illegal = True
        self.array = list(reversed(array))

    def __str__(self):
        return ''.join(reversed(self.array))
    
    def inc(self):
        carry = True
        for i,d in enumerate(self.array):
            if not carry:
                break
            carry = d=='z'
            self.array[i] = Password.incrementer[d]
        if carry:
            self.array = [ord('a')] + self.array
        return bool(self)

    def __bool__(self):
        return any(a==b and c==d for (i,(a,b)) in enumerate(pairwise(self.array)) for (c,d) in pairwise(self.array[i+2:])) \
            and any(ord(c)==ord(b)-1 and ord(b)==ord(a)-1 for a,b,c in zip(self.array,self.array[1:],self.array[2:]))


oldpass = sys.stdin.readlines()[0].strip()
#print(f'*0:',oldpass)

password = Password(oldpass)
while not password.inc():
    pass
print(f'*1: {password}')

while not password.inc():
    pass
print(f'*2: {password}')
